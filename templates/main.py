from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

# Read and substitute the HTML template
html_template = Template(Path("templates/index.html").read_text())
html_content = html_template.substitute({'name': 'Maksim', 'date': 'tomorrow'})

# Create and configure the email message
my_email = EmailMessage()
my_email['From'] = 'Maksim Levanovich <maxlevanovich@gmail.com>'
my_email['To'] = 'maxlevanovich@gmail.com'
my_email['Subject'] = "email with image!"
my_email.set_content(html_content, 'html')

with open('images/email.jpeg', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='jpeg', filename='email.jpeg')

# Send the email
try:
    with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
        smtp_server.ehlo()
        # Remove or comment out the next line if STARTTLS is not supported
        # smtp_server.starttls()
        smtp_server.login('username', 'password')
        smtp_server.send_message(my_email)
        print('Email was sent!')
except Exception as e:
    print(f'Error: {e}')
