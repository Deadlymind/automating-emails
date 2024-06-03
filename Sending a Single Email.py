import yagmail
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(sender, receiver, subject, content, password):
    """
    Send an email using yagmail.

    Parameters:
    sender (str): The email address of the sender.
    receiver (str): The email address of the receiver.
    subject (str): The subject of the email.
    content (str): The content of the email.
    password (str): The password for the sender's email account.
    """
    try:
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=content)
        logging.info('Email sent successfully!')
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

if __name__ == "__main__":
    sender = 'oussamaayari2014@gmail.com'
    receiver = 'fkm3wdjy@minimail.gq'
    subject = 'Automating Emails with Python'
    content = "Hello, here is the content of the email! zz"
    password = 'your_gmail_app_password'

    send_email(sender, receiver, subject, content, password)
