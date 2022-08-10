from PIL import Image, ImageDraw, ImageFont

font = "Poppins-Black.ttf"
fontSize = 100
words = []


def imageCreate(text):

    image = Image.open("bg-layer.jpg")
    font_type = ImageFont.truetype(font=font, size=fontSize)
    # image = image.resize((1920,1080))
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font_type)

    x = (image.width/2) - (text_width/2)
    y = (image.height/2) - (text_height)

    draw.text(xy=(x, y), text=text.upper(),
              fill=(255, 255, 255), font=font_type)

    image.save("output/"+text.lower()+".jpg", quality=50)


for word in words:
    imageCreate(word)
