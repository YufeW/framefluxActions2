import email
import smtplib

def send_email(sender, password, recipient, subject, message):
    msg = email.message_from_string(message)
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    s = smtplib.SMTP("smtp.live.com",587)
    s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    s.starttls() #Puts connection to SMTP server in TLS mode
    s.ehlo()
    s.login(sender, password)

    s.sendmail(sender, recipient, msg.as_string())

    s.quit()

sender = 'antalyze2021@outlook.com'
password = 'Simulation2021!'
recipient = 'yufe@frameflux.nl'
subject = '4'
message = '5'

send_email(sender, password, recipient, subject, message)
