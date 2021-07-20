# Program to write a text on cert.png using Pillow
#
from utils.image import generateCertImage
from utils.email import send_mail

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'


if __name__ == '__main__':
    # Open image
    # generateCertImage(name='Arnab Sen', certificate=CERTIFICATE, event=EVENT)
    send_mail()
    print("mail sent")
