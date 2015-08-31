"""
Python Logging Library

@author: Clivern U{hello@clivern.com}
"""
import smtplib
from email.mime.text import MIMEText


class Mailer():
    """ Send Log Messages To Email """

    def __init__(self, host='smtp.gmail.com', port=587):
        """ Define Host """
        self.host = host
        self.port = port
        self._usr = None
        self._pwd = None

    def login(self, usr, pwd):
        """ Use login() to Log in with a username and password. """
        self._usr = usr
        self._pwd = pwd

    def send(self, me, to, subject, msg):
        """ Send Message """
        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = to
        server = smtplib.SMTP(self.host, self.port)
        server.starttls()
        # Check if user and password defined
        if self._usr and self._pwd:
            server.login(self._usr, self._pwd)
        try:
            # Send email
            server.sendmail(me, [x.strip() for x in to.split(",")], msg.as_string())
        except:
            # Error sending email
            raise Exception("Error Sending Message.")
        # Quit!
        server.quit()