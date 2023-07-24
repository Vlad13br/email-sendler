import smtplib
from email.mime.text import MIMEText


def send_email(recipient, message):
    sender = "alexrozanov11@gmail.com"
    password = "hhzapcyvtlyujuzc"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, recipient, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    recipient = input("Type email")
    message = input("Type your message")
    print(send_email(recipient=recipient, message=message))


if __name__ == "__main__":
    main()
