# Email-automation


Este script automatiza o envio de um relatório diário por e-mail às 6h00 da manhã todos os dias. O script utiliza a biblioteca `schedule` para agendar a execução da função `daily_reports` no horário especificado.

## Requisitos

* Instale a biblioteca `schedule` usando pip: `pip install schedule`

## Configuração

Substitua os valores de placeholder para `your_password` e `recipient_email` com suas credenciais reais.

## Executando o script

Salve o script como um arquivo `.py` e execute-o usando Python. O script continuará a ser executado em segundo plano, verificando o horário agendado para enviar o relatório diário por e-mail.

## Decomposição do script

1. **Importar bibliotecas necessárias:**

   * `smtplib`: Fornece funções para enviar e-mails usando o protocolo SMTP.
   * `MIMEText`: Cria objetos MIME de texto simples para o conteúdo do e-mail.
   * `MIMEMultipart`: Cria objetos MIME multiparte para combinar diferentes tipos de conteúdo.
   * `schedule`: Fornece funções para agendar tarefas para serem executadas em horários específicos.
   * `time`: Fornece funções para operações relacionadas a tempo.

2. **Definir a função `send_email`:**

   * Cria um objeto de mensagem MIMEMultipart.
   * Define o remetente, destinatário e assunto do e-mail.
   * Anexa um objeto MIMEText com o corpo do e-mail.
   * Conecta-se ao servidor SMTP, usando uma conexão segura com TLS.
   * Autentica-se com o endereço de e-mail e senha fornecidos.
   * Envia o e-mail para o destinatário especificado.

3. **Definir a função `daily_reports`:**

   * Define o conteúdo do relatório diário por e-mail, incluindo assunto e corpo.
   * Chama a função `send_email` para enviar o relatório diário por e-mail.

4. **Agendar a função `daily_reports`:**

   * Configura a agenda para executar a função `daily_reports` todos os dias às 6h00.
   * Entra em um loop infinito para verificar continuamente as tarefas agendadas e executá-las.
   * Usa `time.sleep()` para evitar uso excessivo da CPU.


