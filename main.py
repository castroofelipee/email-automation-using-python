import smtplib
from email.minetext import MIMEText
from email.mime.multipart import MIMEMultipart 
import schedule 
import time 

def send_email(subject,  body, to_email):
    message = MIMEMultipart()
    message['From'] = "castrofelipeee18@gmail.com"
    message['To'] = to_email
    message['subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com',  587) as server: 
        server.starttls()

        server.login('castroofelipeee8@email.com'  'your_password')

        server.sendemail('pythonlearningpessoal@gmail.com')
        to_email, message.as_string()

        def daily_reports():
            report_subject = "Daily Report"
            report_body = "Your daily report content goes here."
            recipient_email = "castroofelipee19@gmail.com"

            send_email(report_subject, report_body, recipient_email)

            schedule.every().day.at("06:00").do("daily_report")

            while True:
                schedule.run_pending()
                time.sleep(1)