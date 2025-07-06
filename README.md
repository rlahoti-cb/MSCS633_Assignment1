### MSCS 633 Assignment 1

The script requires us to install the qrcode library dependency with:

```bash
pip3 install qrcode[PIL]
```

In order to run the script to generate the QR code for "https://www.bioxsystems.com/" URL:

```bash
python3 qr_code_generator.py
```

This will generate a QR code for the URL and output the code to a file named `biox-systems-qr.png`.