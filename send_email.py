import smtplib, ssl

# any smtp issues like SSL: CERTIFICATE_VERIFY_FAILED certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
# see https://stackoverflow.com/questions/77442172/ssl-certificate-verify-failed-certificate-verify-failed-unable-to-get-local-is


def send_email(message):

    # for SMTP credentials, including host, port, username / password and
    # receiver - talk to Declan Hurney
    host = "xxxx.xxxxx.xxx"
    port = xxx

    username = "xxxxxxxxxxxx@xxxxx.xxx"
    password = "xxxxxxxxxxxxxxxx"

    receiver = "xxxxxxxxxxxx@xxxxx.xxx"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

# send_email("Hello, how are you?")
