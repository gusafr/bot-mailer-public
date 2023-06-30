import smtplib
import csv
import logging
import os
import configparser
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Lendo o arquivo de configuração
config = configparser.ConfigParser()
config.read('config.ini')

# Configurações do servidor de email
smtp_server = config.get('SMTP', 'server')
port = config.getint('SMTP', 'port')
username = config.get('SMTP', 'username')
password = config.get('SMTP', 'password', raw=True)

# Configurações do email
subject = config.get('Email', 'subject')
template_file = config.get('Email', 'template_file')

# Leitura do arquivo de template
with open(template_file, 'r', encoding='utf-8') as f:
    template = f.read()

# Diretório e nome do arquivo de log
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f'email_sending_{current_time}.log')

# Configuração de log
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Listas para armazenar emails de sucesso e erro
successful_emails = []
failed_emails = []

# Leitura do arquivo CSV
with open(os.path.join('input', 'input.csv'), 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        to_email, to_name = row

        # Criando a mensagem
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Substituindo a tag {name} no template pelo nome do destinatário
        message = template.replace('{name}', to_name)

        msg.attach(MIMEText(message, 'html'))

        # Enviando o email
        try:
            server = smtplib.SMTP_SSL(smtp_server, port)
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, to_email, text)
            server.quit()

            logging.info(f'Email enviado para {to_email}')
            successful_emails.append(to_email)

        except Exception as e:
            logging.error(f'Falha ao enviar email para {to_email}: {str(e)}')
            failed_emails.append(to_email)

# Salvando emails de sucesso e erro em arquivos de texto
with open(os.path.join('output', 'successful_emails.txt'), 'w') as f:
    for email in successful_emails:
        f.write(f'{email}\n')

with open(os.path.join('output', 'failed_emails.txt'), 'w') as f:
    for email in failed_emails:
        f.write(f'{email}\n')

# Mover o arquivo de input para um diretório de processados
processed_dir = 'processed'
os.makedirs(processed_dir, exist_ok=True)
shutil.move(os.path.join('input', 'input.csv'), os.path.join(processed_dir, 'input.csv'))
