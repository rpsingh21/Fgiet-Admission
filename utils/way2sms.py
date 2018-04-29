import requests
from bs4 import BeautifulSoup
from fgietAdmission.secret import smsCred

class Sms():
	def __init__(self):
		self.url='http://site21.way2sms.com/Login1.action?'
		self.cred={'username': smsCred["username"], 'password': smsCred["password"]}
		self.s=requests.Session()
		self.s.headers['User-Agent']="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"

		self.q=self.s.post(self.url,data=self.cred)

		self.loggedIn=False	

		if "http://site21.way2sms.com/main.action" in self.q.url:
			# print("Successfully logged in..!")
			self.loggedIn=True
		else:
			print("Can't login, once check credential..!")
			self.loggedIn=False
		self.jsid=self.s.cookies.get_dict()['JSESSIONID'][4:]	   

	def msgSentToday(self):
		if self.loggedIn == False:
			print("Can't perform since NOT logged in..!")
			return -1

		self.msg_left_url='http://site21.way2sms.com/sentSMS?Token='+self.jsid
		self.q=self.s.get(self.msg_left_url)
		self.soup=BeautifulSoup(self.q.text,'html.parser')
		self.t=self.soup.find("div",{"class":"hed"}).h2.text
		self.sent=0

		for self.i in self.t:
			if self.i.isdecimal():
				self.sent=10*self.sent+int(self.i)

		return self.sent

	def send(self,mobile_no,msg):
		if self.loggedIn == False:
			print("Can't perform since NOT logged in..!")
			return False
		if len(msg)>139 or len(mobile_no)!=10 or not mobile_no.isdecimal():
			return False

		self.payload={'ssaction':'ss',
				'Token':self.jsid,
			        'mobile':mobile_no,
       				 'message':msg,
			        'msgLen':'129'
       			     }
		self.msg_url='http://site21.way2sms.com/smstoss.action'
		self.q=self.s.post(self.msg_url,data=self.payload)
		if self.q.status_code==200:
			return True
		else:
			return False

	def logout(self):
		self.s.get('http://site21.way2sms.com/entry?ec=0080&id=dwks')
		self.s.close()
		self.loggedIn=False
