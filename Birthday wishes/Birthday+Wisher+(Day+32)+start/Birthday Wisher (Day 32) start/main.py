
# Sending Emails

import smtplib
my_email="guptaanuj0812"
passward="gqqtssunqymavwrp"
with smtplib.SMTP("smtp.gmail.com") as connection
    connection.starttls()
    connection.login(user=my_email,password=passward)
    connection.sendmail(from_addr=my_email,
                        to_addrs="anujgupta0333@gmail.com",
                        msg="Subject:Hello\n\nthis is me")
