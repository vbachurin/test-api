import unittest
import requests
from yaml import load
from base_test import BaseAPITest

class TestDeleteIssue(BaseAPITest):
	
	def setUp(self):
		super(TestDeleteIssue, self).setUp()
		self.url = self.base_url + '/issue/'

	def test_new_issue(self):
		issue_id = self.create_issue()

		r = requests.delete(self.url + issue_id, cookies=self.cookies)

		self.assertEquals(r.status_code, 200)

		r = requests.get(self.url + issue_id, cookies=self.cookies)
		self.assertEquals(r.status_code, 404)
