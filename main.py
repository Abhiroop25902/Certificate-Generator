# Program to write a text on cert.png using Pillow
#
import smtplib
from utils.image import generateCertImage
from utils.email import send_mail
from utils import file_reader

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'
LOGIN_CREDENTIAL_FILE = './login_credential.txt'
CONTACT_LIST_FILE = 'contactList.txt'
MESSSAGE_FORMAT_FILE = 'message.txt'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# import the smtplib module. It should be included in Python by default


if __name__ == '__main__':
    # Open image
    # generateCertImage(name='Arnab Sen', certificate=CERTIFICATE, event=EVENT)

    # set up the SMTP server
    s = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    s.starttls()

    credential = file_reader.read_credential(LOGIN_CREDENTIAL_FILE)
    s.login(credential[0], credential[1])

    names, dest_emails = file_reader.get_contacts(
        CONTACT_LIST_FILE)  # read contact
    message_template = file_reader.read_template(MESSSAGE_FORMAT_FILE)

    # For each contact, send the email:
    for name, dest_email in zip(names, dest_emails):
        send_mail(s, message_template, name, dest_email,
                  src_email=credential[0], image_file = CERTIFICATE)
    print("mail sent")
