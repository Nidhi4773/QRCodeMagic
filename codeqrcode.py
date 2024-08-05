import qrcode
import random
import string
from PIL import Image

def generate_random_data(length=10):
    #Generate random alphanumeric data.
    letters_and_digits=string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def create_qr_code(data):
    #Create a Qr code from the given data.
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    return img

if __name__=="__main__":
    random_data=generate_random_data()
    qr_image= create_qr_code(random_data)

    #Save the Qrcode as an image(optional)
    #qr_image.save("random_qr_code.png")

    #Display the Qr code image using PIL
    qr_image.show()

    print(f"Generate QR code with data: {random_data}")


    
