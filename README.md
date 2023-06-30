# Python Email Sender Script 
Este script Python envia e-mails personalizados para uma lista de destinatários. A lista de destinatários e seus nomes são lidos de um arquivo CSV de entrada. O script utiliza um arquivo HTML como template para as mensagens de e-mail. Ele também registra a atividade em um arquivo de log e cria listas de e-mails enviados com sucesso e de erros.

# Pré-requisitos
Python 3.8 ou superior
Acesso a um servidor SMTP (este exemplo utiliza o serviço do GoDaddy)
Configuração
Clone este repositório para o seu computador.

Instale as bibliotecas necessárias usando o pip. Execute o seguinte comando no terminal:

bash
pip install configparser
Crie um arquivo config.ini na raiz do projeto com as configurações do servidor SMTP e do e-mail. O arquivo deve ter a seguinte estrutura:

ini
[SMTP]
server = smtpout.secureserver.net
port = 465
username = seu_username@godaddy.com
password = sua_senha

[Email]
subject = Assunto do Seu Email
template_file = templates/template.html
Substitua seu_username@godaddy.com e sua_senha pelas suas credenciais do GoDaddy. template_file é o caminho para o arquivo HTML que você quer usar como template para os e-mails.

Crie o arquivo HTML de template em templates/template.html. Este arquivo deve ser um HTML válido. Você pode incluir {name} em qualquer lugar que deseja que o nome do destinatário apareça.

Crie um arquivo CSV de entrada em input/input.csv. Este arquivo deve ter dois campos: endereço de e-mail e primeiro nome. Aqui está um exemplo de como o arquivo deve ser:

csv
joao@example.com,João
maria@example.com,Maria
carlos@example.com,Carlos

Execução
Execute o script Python no terminal com o seguinte comando:

bash
python email_sender.py
O script irá enviar um e-mail para cada linha do arquivo CSV. Ele criará um arquivo de log em logs/ com informações sobre cada e-mail enviado. Também criará listas de e-mails enviados com sucesso e de erros em output/.

Após o processo, o arquivo CSV de entrada será movido para a pasta processed/.

# Suporte
Para suporte ou quaisquer outras dúvidas, por favor abra uma issue neste repositório.

