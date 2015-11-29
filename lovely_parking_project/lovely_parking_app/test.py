import json

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from lovely_parking_project.lovely_parking_app.models import Location

class UserTests(APITestCase):
	url = '/users/'
	
	def setUp(self):
		self.user = User.objects.create(id=0, username='testuser', password='testpassword')
		self.token = Token.objects.get(user=self.user)
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
	
	def test_create_user(self):
		data = {
			'username': 'user1',
			'email': 'testemail@email.com',
			'password': 'password'
		}
		response = self.client.post(self.url, data)
		self.assertEqual(response.status_code, 201)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['username'], data['username'])
		self.assertEqual(result_json['email'], data['email'])

		self.assertEqual(User.objects.count(), 2)
		
		database_obj = User.objects.get(username=data['username'])
		self.assertEqual(database_obj.email, data['email'])
		
	def test_read_users(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)[0]
		self.assertEqual(result_json['username'], self.user.username)
		self.assertEqual(result_json['email'], self.user.email)
	
	def test_read_one_user(self):
		response = self.client.get(self.url + '0/')
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['username'], self.user.username)
		self.assertEqual(result_json['email'], self.user.email)
	
	def test_update_user(self):
		data = {
			'username': 'user2',
			'email': 'testemail2@email.com'
		}
		response = self.client.put(self.url + '0/', data)
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['username'], data['username'])
		self.assertEqual(result_json['email'], data['email'])
		
		database_obj = User.objects.get(id=0)
		self.assertEqual(database_obj.username, data['username'])
		self.assertEqual(database_obj.email, data['email'])
		
	def test_destroy_user(self):
		response = self.client.delete(self.url + '0/')
		self.assertEqual(response.status_code, 204)
		
		self.assertEqual(User.objects.count(), 0)
		
	def test_unauth(self):
		self.client.credentials()
		
		data = {
			'username': 'user1',
			'email': 'testemail@email.com',
			'password': 'password'
		}
		response = self.client.post(self.url, data)
		self.assertEqual(response.status_code, 401)
		
	def tearDown(self):
		self.user.delete()
		self.token.delete()
		self.client.credentials()
		
class LocationTests(APITestCase):
	url = '/locations/'
	
	def setUp(self):
		self.user = User.objects.create(id='0', username='testuser', password='testpassword')
		self.token = Token.objects.get(user=self.user)
		self.location = Location.objects.create(id='0', name='testlocation', address='testaddress', coordinates='(1.000, -1.000)')
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
	
	def test_create_location(self):
		data = {
			'name': 'testlocation2',
			'address': 'testaddress2',
			'coordinates': '(0.000, 0.000)'
		}
		response = self.client.post(self.url, data)
		self.assertEqual(response.status_code, 201)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['name'], data['name'])
		self.assertEqual(result_json['address'], data['address'])
		self.assertEqual(result_json['coordinates'], data['coordinates'])

		self.assertEqual(Location.objects.count(), 2)
		
		database_obj = Location.objects.get(name=data['name'])
		self.assertEqual(database_obj.address, data['address'])
		self.assertEqual(database_obj.coordinates, data['coordinates'])
		
	def test_read_locations(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)[0]
		self.assertEqual(result_json['name'], self.location.name)
		self.assertEqual(result_json['address'], self.location.address)
		self.assertEqual(result_json['coordinates'], self.location.coordinates)
	
	def test_read_one_location(self):
		response = self.client.get(self.url + '0/')
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['name'], self.location.name)
		self.assertEqual(result_json['address'], self.location.address)
		self.assertEqual(result_json['coordinates'], self.location.coordinates)
	
	def test_update_location(self):
		data = {
			'name': 'testlocation2',
			'address': 'testaddress2',
			'coordinates': '(0.000, 0.000)'
		}
		response = self.client.put(self.url + '0/', data)
		self.assertEqual(response.status_code, 200)
		
		result_json = json.loads(response.content)
		self.assertEqual(result_json['name'], data['name'])
		self.assertEqual(result_json['address'], data['address'])
		self.assertEqual(result_json['coordinates'], data['coordinates'])

		database_obj = Location.objects.get(id=0)
		self.assertEqual(database_obj.name, data['name'])
		self.assertEqual(database_obj.address, data['address'])
		self.assertEqual(database_obj.coordinates, data['coordinates'])
		
	def test_destroy_location(self):
		response = self.client.delete(self.url + '0/')
		self.assertEqual(response.status_code, 204)
		
		self.assertEqual(User.objects.count(), 1)
		
	def test_unauth(self):
		self.client.credentials()
		
		data = {
			'name': 'testlocation2',
			'address': 'testaddress2',
			'coordinates': '(0.000, 0.000)'
		}
		response = self.client.post(self.url, data)
		self.assertEqual(response.status_code, 401)
		
	
	def tearDown(self):
		self.user.delete()
		self.token.delete()
		self.location.delete()
		self.client.credentials()