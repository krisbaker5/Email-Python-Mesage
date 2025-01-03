# Email Automation with Python

This project demonstrates a simple email automation script written in Python. The script utilizes the `smtplib` library to send emails from a Gmail account to a specified recipient.

## Features

- Automates sending personalized emails.
- Uses Python's built-in libraries: `smtplib`, `email.mime`, and `ssl`.
- Includes error handling to ensure the email is sent securely.
  
## Prerequisites

Before running the script, make sure you have:

- A Gmail account (or an email service provider that allows SMTP access).
- Enabled "Less Secure Apps" for your Gmail account or set up an App Password (for 2FA enabled accounts).]

  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/<your-repository>.git
    ```

2. Install any dependencies:

    This project uses Python's built-in libraries, so no additional installations are required.

## Usage

1. Download the `send_email.py` script.
2. Replace the following placeholders in the script:
    - `your_email@gmail.com` with your email address.
    - `your_password` with your email password (or app password if 2FA is enabled).
    - `recipient_email@example.com` with the recipient's email address.
3. Run the script to send the email:

    ```bash
    python send_email.py
    ```

## Example

Here’s a preview of the email sent by the script:

```text
Subject: Hello, from Python!

Hi there!

This is an automated email sent using Python!

Best regards,
Your Name
