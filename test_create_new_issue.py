import unittest
import requests
from yaml import load
from base_test import BaseAPITest

class TestGetIssue(BaseAPITest):


	def setUp(self):
		super(TestGetIssue, self).setUp()
		self.url = self.base_url + '/issue/'

	def test_new_issue(self):
	

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
		
	def test_new_issue_with_incorrect_project(self):
		params = {
			'project': 'INVALIDAPI',
			'summary': 'mysumm',
			'description': ' mydesc'
		}		
		r = requests.put(self.url, data=params, cookies=self.cookies)
		self.assertEquals(r.status_code, 403)