#!/usr/bin/python

# Developed by: Pedro Manuel Alves Sanches on 04/12/2020

# libraries
import subprocess
import shlex
from datetime import datetime
import getpass
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function that allow the arguments to be executed as command lines. The result of that is returned as text
def execute_command_line(arguments):
    return subprocess.run(arguments, shell=True, capture_output=True, text=True)


# Function that create a string with the current datetime information
def get_current_date_time():
    return datetime.now().strftime("_%d_%m_%Y_%H_%M_%S_")


# Function that create and write into a file. Then returns the filename
def write_into_txt(text):
    filename = "result" + get_current_date_time() + ".txt"
    f = open(filename, "w")
    f.write(text)
    f.close()
    return filename


# Function that allow the user to insert a valid command line
def get_command_line():
    command_line = input("Enter command line: ")
    while len(command_line) == 0:
        command_line = input("Enter command line: ")
    return shlex.split(command_line)


# Function create and send an email with an attachment.
# IMPORTANT: only Gmails can be used in the 'From' field.
#            The email sends an attachment with the returned result of the executed command.
#            The email used must have the definition: "Allow less secure apps" turned ON
def send_email(filename):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = input("From: ")
    message["To"] = input("To: ")
    message["Subject"] = input("Subject: ")
    body = input("Body: ")
    password = getpass.getpass()

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(message["From"], password)
        server.sendmail(message["From"], message["To"], text)


array = get_command_line()
while array[0] != "exit":

    p1 = execute_command_line(array)

    if p1.returncode == 0:
        file = write_into_txt(p1.stdout)
        send_email(file)
    else:
        print("Command Invalid")

    array = get_command_line()
