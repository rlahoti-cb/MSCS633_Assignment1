import qrcode

# helper function which generates a QR code for a given URL 
def generate_qr_code(url, output_file):
    # initialize an instance of the QRCode class
    # version controls size of QR code with size 1 generating a 21x21 matrix
    # box size controls the number of pixels each box in the QR code is
    # border controls how many boxes thick the border is
    qr_gen = qrcode.QRCode(version=1, box_size=50, border=5)

    # supply URL to instance of QR code
    qr_gen.add_data(url)

    # generates the QR code
    qr_gen.make()

    # generates the image for the QR code
    image = qr_gen.make_image(fill_color="black", back_color="white")

    # save image to output file
    image.save(output_file)
    print("Generated image for URL \'" + url + "\' in image " + output_file)

if __name__ == "__main__":
    # inputs for the QR code generation
    url = "https://www.bioxsystems.com/"
    output_file = "biox-systems-qr.png"

    # call helper function to generate QR code
    generate_qr_code(url, output_file)