import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv
import os

class MailService:
    # Load environment variables from the .env file
    load_dotenv()

    def __init__(self, content):
        self.content = content

    def send_mail(self):
        # Get today's date
        date = datetime.today().strftime('%d-%m-%Y')

        # Subject and HTML body content
        subject = f"Stanovi na Novom Beogradu {date}"

        """Generate HTML email body with a table"""
        # Define CSS styles for the table
        table_css = """
               <style>
                   table {
                       border-collapse: collapse;
                       width: 100%;
                   }
                   th, td {
                       border: 1px solid #dddddd;
                       text-align: left;
                       padding: 8px;
                   }
                   th {
                       background-color: #f2f2f2;
                   }
               </style>
               """
        body = f"""
        <html>
        <head>
            {table_css}
        </head>
        <body>
            </br>
            <h2>Stanovi na Novom Beogradu  {datetime.today().strftime('%d-%m-%Y')}</h2>
            <p>Tabela stanova:</p>
            {self.content}
            </br>
        </body>
        </html>
        """

        # Email sender and receiver
        sender_email = os.getenv("EMAIL")
        receiver_email = os.getenv("RECEIVER")
        password = os.getenv("PASSWORD_MAIL")

        if not password:
            print("Error: Email password not found in environment variables.")
            return

        # Create a MIMEMultipart message object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach HTML content to the email body
        msg.attach(MIMEText(body, 'html'))  # Changed to 'html' instead of 'plain'

        # Set up the SMTP server and send the email
        try:
            # Connect to Gmail's SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Encrypt the connection
                server.login(sender_email, password)  # Login to the server

                # Send the email
                server.sendmail(sender_email, receiver_email, msg.as_string())
                print("Email sent successfully!")

        except smtplib.SMTPException as e:
            print(f"SMTP error: {e}")
        except Exception as e:
            print(f"Error: {e}")