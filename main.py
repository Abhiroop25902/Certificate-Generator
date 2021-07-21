# Program to write a text on cert.png using Pillow
# import the smtplib module. It should be included in Python by default
import smtplib
from utils.image import generateCertImage
from utils.mail import Email
import os
from dotenv import load_dotenv, find_dotenv

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'
CONTACT_LIST_FILE = './participants.csv'
EMAIL_BODY_TEMPLATE = './message.txt'

SUBJECT = "Certificate of Portfolio Contest"

if __name__ == '__main__':
    load_dotenv(find_dotenv())

    EMAIL = os.environ.get("EMAIL")
    PASSWORD = os.environ.get("PASSWORD")

    message_template = open(EMAIL_BODY_TEMPLATE, 'r').read()

    emailObj = Email(EMAIL, PASSWORD)

    # read names and email from participants.csv
    with open(CONTACT_LIST_FILE, 'r') as f:
        for details in f.readlines():
            name, email = details.split(',')
            name = name.strip()
            email = email.strip()
            body = message_template.format(name=name)
            cert_name = generateCertImage(
                name=name, event=EVENT, certificate=CERTIFICATE, output_dir='./certificates')
            emailObj.sendEmail(subject=SUBJECT, body=body, to=email,
                               from_email=EMAIL, attachments=[cert_name])

            print("Mail sent to {name} # {email}".format(
                name=name, email=email))

    emailObj.close()
