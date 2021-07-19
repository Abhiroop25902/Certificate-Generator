# Program to write a text on cert.png using Pillow
#
from utils.image import generateCertImage

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'


if __name__ == '__main__':
    # Open image
    generateCertImage(name='Arnab Sen', certificate=CERTIFICATE, event=EVENT)
