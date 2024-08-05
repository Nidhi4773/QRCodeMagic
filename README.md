# QRCodeMagic
## Overview
This project is a simple QR code generator written in Python. It generates unique alphanumeric strings and creates corresponding QR codes that can be saved as images and displayed on the screen. This application can be useful for various purposes, such as generating unique identifiers for certificates, links, or other data where QR codes can be utilized.

## Features
- Generates random alphanumeric data.
- Creates a QR code based on the generated data.
- Optionally saves the QR code as an image file (PNG).
- Displays the generated QR code using the PIL (Pillow) library.

## Requirements
- Python 3.x
- `qrcode` library
- `Pillow` (PIL) library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nidhi4773/QRCodeMagic.git
   ```

2. **Install required libraries**:
   You can use pip to install the necessary libraries:
   ```bash
   pip install qrcode[pil] Pillow
   ```

## Usage

1. Open your terminal or command prompt.
2. Run the Python script:
   ```bash
   python codeqrcode.py
   ```
3. The script will generate random alphanumeric data, create a QR code image based on that data, and save it as `random_qr_code.png` in the same directory. The QR code image will also be displayed on your screen.
4. Check the terminal for the generated data message.

## Example
When you run the script, the output will look like this:

```
Generated QR code with data: al2dF3gT9J
```
And you will see an image pop up displaying the QR code corresponding to the generated data.

## Customization
You can adjust the length of the random data by modifying the `length` parameter in the `generate_random_data()` function call within the `if __name__ == "__main__":` block. 

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments
- Thanks to the contributors and the open-source community for their libraries and support.

## Contact
For any inquiries or support, please contact me at nknidhii05@gmail.com


