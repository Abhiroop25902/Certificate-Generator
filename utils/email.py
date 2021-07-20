# import the smtplib module. It should be included in Python by default
import smtplib

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils import file_reader


def send_mail():
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.ehlo()
    s.starttls()

    credential = file_reader.read_credential('login_credential.txt')
    s.login(credential[0], credential[1])

    names, emails = file_reader.get_contacts('contactList.txt')  # read contact
    message_template = file_reader.read_template('message.txt')

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = credential[0]
        msg['To'] = email
        msg['Subject'] = "This is TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg
