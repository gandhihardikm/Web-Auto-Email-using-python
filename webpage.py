from six.moves import urllib
import smtplib
page = urllib.request.urlopen('http://engineering.sjsu.edu/news-and-events/events')
print("response received")
html1 = page.read()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "Receiver's email address "

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Upcoming Event"
msg['From'] = me


# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow you?\nHere is the link you wanted:\nhttp://www.python.org"
html = html1

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')


# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('Your email address', 'Your Email password')
mail.sendmail(me, pankaj, msg.as_string())

mail.quit()
