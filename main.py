# Program to write a text on cert.png using Pillow
# import the smtplib module. It should be included in Python by default
import smtplib
from utils.image import generateCertImage
from utils.email import send_mail
from utils import file_reader
import os
from dotenv import load_dotenv, find_dotenv

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'
CONTACT_LIST_FILE = './participants.csv'
MESSSAGE_FORMAT_FILE = './message.txt'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587


MAIL_SUBJECT = "This is TEST"
CC = "abhiroopgamer@gmail.com, abc@example.com"
BCC = "510519109.abhirup@students.iiests.ac.in, bcd@example.com"


if __name__ == '__main__':

    # set up the SMTP server
    s = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    s.starttls()

    # read credential from a safe file(added in .gitignore) and login using that
    load_dotenv(find_dotenv())
    EMAIL = os.environ.get("EMAIL")
    PASSWORD = os.environ.get("PASSWORD")

    s.login(EMAIL, PASSWORD)

    # read contact details and message template
    names, dest_emails = file_reader.get_contacts(
        CONTACT_LIST_FILE)  # read contact
    message_template = file_reader.read_template(MESSSAGE_FORMAT_FILE)

    # For each contact, send the email:
    for participant_name, dest_email in zip(names, dest_emails):

        # captalizing the name
        participant_name = participant_name.capitalize()

        # Generate image certificate
        image_filename = generateCertImage(
            name=participant_name, certificate=CERTIFICATE, event=EVENT)

        # send email to the contact
        send_mail(s, message_template, participant_name, dest_email,
                  src_email=EMAIL, mail_subject=MAIL_SUBJECT, image_file=image_filename,
                  cc=CC, bcc=BCC)

        # delete the image certificate generated
        os.remove(image_filename)

    print("mail sent")
