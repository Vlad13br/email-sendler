import smtplib
from email.mime.text import MIMEText


def send_email(recipient):
    sender = ""  # Your email
    password = ""  # Your password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open("email_template.html") as file:
            template = file.read()
    except IOError:
        return "The template file doesn`t found"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, recipient, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    recipient = input("Type email")
    print(send_email(recipient=recipient))


if __name__ == "__main__":
    main()
