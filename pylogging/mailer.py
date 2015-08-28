import smtplib
from email.mime.text import MIMEText

class Mailer():
    """ Used By Logger to Send Emails """

    def __init__(self, host="localhost"):
        """ Define Host """
        self.host = host
        self._usr = None
        self._pwd = None

    def login(self, usr, pwd):
        """ Use login() to log in with a username and password. """
        self._usr = usr
        self._pwd = pwd

    def send(self, me, to, subject, msg):
        """ Send Message """
        msg = MIMEText(msg)
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = to
        server = smtplib.SMTP(self.host)
        if self._usr and self._pwd:
            server.login(self._usr, self._pwd)
        try:
            server.sendmail(me, [x.strip() for x in to.split(",")], msg.as_string())
        except:
            raise Exception("Error Sending Message.")
        server.quit()