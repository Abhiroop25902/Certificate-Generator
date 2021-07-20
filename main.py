# Program to write a text on cert.png using Pillow
#
from utils.image import generateCertImage

EVENT = 'Portfolio-Contest'
CERTIFICATE = './cert.png'


if __name__ == '__main__':

    # Read participants.csv and generate a list of names
    details = []
    with open('./participants.csv', 'r') as f:
        for line in f:
            details.append(line.split(','))

    for name, email in details:
        generateCertImage(name=name, output_dir='certificates',
                          certificate=CERTIFICATE, event=EVENT)
