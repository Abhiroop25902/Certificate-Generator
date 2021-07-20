# Program to write a text on cert.png using Pillow
#
import smtplib
from utils.image import generateCertImage
from utils.email import send_mail
from utils import file_reader
import os

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'
LOGIN_CREDENTIAL_FILE = './login_credential.txt'
CONTACT_LIST_FILE = './participants.csv'
MESSSAGE_FORMAT_FILE = './message.txt'
MAIL_SUBJECT = "This is TEST"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# import the smtplib module. It should be included in Python by default


if __name__ == '__main__':

    # set up the SMTP server
    s = smtplib.SMTP(host=EMAIL_HOST, port=EMAIL_PORT)
    s.starttls()

    # read credential from a safe file(added in .gitignore) and login using that
    credential = file_reader.read_credential(LOGIN_CREDENTIAL_FILE)
    s.login(credential[0], credential[1])

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
                  src_email=credential[0], mail_subject= MAIL_SUBJECT, image_file=image_filename)

        # delete the image certificate generated
        os.remove(image_filename)

    print("mail sent")
