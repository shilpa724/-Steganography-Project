
# Secure Data Hiding in Images Using Steganography

## Introduction
This project implements steganography using the Least Significant Bit (LSB) technique to hide and retrieve messages in images. It features a simple GUI built with Tkinter, allowing users to securely embed and extract hidden messages.

## Technologies Used
- **Python** – Core programming language
- **Tkinter** – GUI framework
- **Pillow (PIL)** – Image processing
- **Bit Manipulation** – Encoding and decoding messages using binary operations

## System Requirements
- **Operating System**: Windows, macOS, or Linux
- **Python Version**: Python 3.x
- **RAM**: Minimum 2GB (4GB recommended)

## Installation Guide
1. **Install Python (if not already installed)**  
   Download and install Python 3 from [Python's official website](https://www.python.org/).

2. **Install Required Packages**  
   Open a terminal or command prompt and run:
   ```sh
   pip install pillow
   ```

## Usage Instructions

### 1. Hiding a Message in an Image
Run the following command to start the message-hiding application:
```sh
python hidden\ msg.py
```
#### Steps:
- Enter the message you want to hide.
- Select an image file.
- Save the modified image with the hidden message.

### 2. Retrieving a Hidden Message
Run the following command:
```sh
python reveal\ msg.py
```
#### Steps:
- Open the saved image with the hidden message.
- The extracted hidden message will be displayed.

## Features
- Uses **LSB (Least Significant Bit) Steganography** for message hiding.
- Simple and easy-to-use GUI.
- The message is **invisible to the human eye**.
- No complex encryption required.

## Future Enhancements
- Support for more file formats (audio, video, text).
- AI-powered detection avoidance techniques.
- Cloud-based real-time integration.

## Contributing
Feel free to submit pull requests or issues to improve the project.
