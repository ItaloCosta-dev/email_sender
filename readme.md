# Automação de E-mails - Envio de Relatórios Automáticos

Este é um projeto em Python para automatizar o envio de e-mails com anexos. O objetivo deste projeto é enviar relatórios ou qualquer outro tipo de documento automaticamente para um ou mais destinatários.

## Funcionalidades

- Envio de e-mails com texto no corpo e anexos (como arquivos PDF).
- Configuração simples de e-mail usando as credenciais de um usuário Gmail.
- Uso de bibliotecas como `smtplib` e `email.mime`.
## Tecnologias Usadas

- **Python 3.x**
- **Bibliotecas**:
  - `smtplib`: para enviar e-mails via SMTP.
  - `email.mime`: para criar e-mails com anexos.
  
```

Além disso, você precisará de uma conta de e-mail Gmail e criar uma senha de aplicativo para permitir o envio de e-mails através do seu script Python. Para mais informações sobre como criar uma senha de aplicativo, consulte [Este link](https://support.google.com/accounts/answer/185833?hl=pt-BR).

## Como Usar

1. **Configuração do Ambiente**:
   Crie um arquivo `.env` no diretório do projeto para armazenar suas variáveis de e-mail. Este arquivo não deve ser compartilhado publicamente, pois contém informações sensíveis.

   Exemplo do conteúdo do arquivo `.env`:
   ```env
   EMAIL_REMETENTE=seuemail@gmail.com
   SENHA=sua_senha_de_app
   EMAIL_DESTINATARIO=destinatario@gmail.com
   ```

2. **Rodando o Script**:
   No terminal, dentro do diretório do projeto, execute o script Python para enviar o e-mail com o anexo:

   ```bash
   python email_sender.py
   ```

   O e-mail será enviado para o destinatário com o anexo especificado no código.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
automatic_email/
├── email_sender.py          # Script para envio de e-mails
├── tecnicas_bjj.pdf         # Exemplo de arquivo PDF para anexar
```

## Problemas Conhecidos

- O envio de e-mails pode ser bloqueado por alguns provedores de e-mail se as configurações de segurança não forem ajustadas corretamente. Para o Gmail, é necessário permitir "Acesso a apps menos seguros" ou configurar uma senha de aplicativo, como mencionado acima.
