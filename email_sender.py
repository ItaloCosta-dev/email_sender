import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Configurações do e-mail
email_remetente = "italosiqueiradacosta@gmail.com"
senha = "wtnm gjet wxqz sxkr"
email_destinatario = "web.lucasvieira@gmail.com"

# Criando o e-mail
mensagem = MIMEMultipart()
mensagem["From"] = email_remetente
mensagem["To"] = email_destinatario
mensagem["Subject"] = "Relatório Automático enviado em Python."

# Corpo do e-mail
corpo = "Olá, segue em anexo o relatório automático gerado."
mensagem.attach(MIMEText(corpo, "plain"))

# Anexando um arquivo
caminho_arquivo = "tecnicas_bjj.pdf"  # Substitua pelo nome do arquivo
with open(caminho_arquivo, "rb") as anexo:
    parte = MIMEBase("application", "octet-stream")
    parte.set_payload(anexo.read())

# Codifica o anexo em base64
encoders.encode_base64(parte)
parte.add_header("Content-Disposition", f"attachment; filename={caminho_arquivo}")
mensagem.attach(parte)

# Conectando ao servidor SMTP e enviando o e-mail
try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(email_remetente, senha)
    servidor.sendmail(email_remetente, email_destinatario, mensagem.as_string())
    servidor.quit()
    print("E-mail enviado com anexo!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")
