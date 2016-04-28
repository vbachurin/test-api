import unittest
import requests
from yaml import load

class BaseAPITest(unittest.TestCase):

	def setUp(self):
		self.settings = load(open('settings.yaml').read())
		self.base_url = self.settings['base_url']

		params = {
			'login': self.settings['credentials']['login'],
			'password': self.settings['credentials']['psswd']
		}

		url = self.base_url + '/user/login'
		r = requests.post(url, data=params)
		self.cookies = r.cookies

	def create_issue(self):
		params = {
			'project': 'API',
			'summary': 'mysumm',
			'description': ' mydesc'
		}

		r = requests.put(self.url, data=params, cookies=self.cookies)
		self.assertEquals(r.status_code, 201)

		issue_id = r.headers['location'].split('/')[-1]
		r = requests.get(self.url + issue_id, cookies=self.cookies)
		self.assertEquals(r.status_code, 200)

		return issue_id