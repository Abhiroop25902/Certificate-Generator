from PIL import Image, ImageFont, ImageDraw


def generateCertImage(name, certificate, font='fonts/Montserrat-Bold.ttf', size=100, height_offset=60, event='CodeIIEST'):
    # Open image
    img = Image.open(certificate)

    width = img.size[0]
    height = img.size[1]

    # Open font
    font = ImageFont.truetype(font=font, size=size)
    # Open Draw
    draw = ImageDraw.Draw(img)

    # Text size of the message
    text_width, text_height = draw.textsize(name, font=font)

    # Write text in the center of the image
    draw.text(((width - text_width) / 2, (height - text_height) / 2 - height_offset),
              name, font=font, fill=(0, 0, 0))

    # Save the image
    img.save('{name}-{event}.png'.format(name=name.replace(' ', '-'), event=event))
