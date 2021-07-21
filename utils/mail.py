# Send email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Email:
    def __init__(self, from_email, password):
        super().__init__()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(from_email, password)
        print('Email logged in successfully...')

    def close(self):
        print('Email quit successfully...')
        self.server.quit()

    def sendEmail(self, subject, body, to, from_email, cc=None, bcc=None, attachments=None):
        """
        Send an email to the given address.
        """

        # Create the message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to
        if cc:
            msg['CC'] = cc
        if bcc:
            msg['BCC'] = bcc
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Attach the attachments
        if attachments:
            for attachment in attachments:
                with open(attachment, "rb") as attachmentFile:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachmentFile.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                                "attachment; filename= %s" % attachment.split('/')[-1])
                msg.attach(part)

        # Send the message
        text = msg.as_string()
        self.server.sendmail(from_email, to, text)
