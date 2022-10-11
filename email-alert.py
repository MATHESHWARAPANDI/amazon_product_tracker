import smtplib
from email.message import EmailMessage

# Python file la values ye irukka koodathu. Ellame thaniya oru file la constant uh irukkanum. illa vera place la irunthu input vaanganum. (like script run pannum pothu input uh vaangalaam. or vera place la irunthu input fetch pannalaam.
# )


# datatype mention pannalaam function parameter la. athaiyum padi. example as below
def dummy_function(product: str, link: str):
    pass


def alert_system(product, link):
    # Ithellam configuration file la add pannalaam.
    email_id = 'ExampleEmail@gmail.com'
    email_pass = 'PasswordHere'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'ExampleEmail@gmail.com'  # receiver address
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)
