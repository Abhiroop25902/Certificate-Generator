

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib
from string import Template
import os


def send_mail(s: smtplib.SMTP, message_template: Template, name: str,
              dest_email: str, src_email: str, image_file: str):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From'] = src_email
    msg['To'] = dest_email
    msg['Subject'] = "This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    with open(image_file, 'rb') as f:
        img_data = f.read()

    image = MIMEImage(img_data, name=os.path.basename(image_file))
    msg.attach(image)

    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
