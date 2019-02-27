"""
Githubscore helper functions

"""
import flask
import githubscore
import requests

from githubscore.model import get_db


def get_stars(repos_url):
	print('get_stars funciton &&&&&&&&&')

	stars = 0

	response = requests.get(repos_url)
	print("Repos API status code: ", response.status_code)
	repos = response.json()
	# print('user_data: ', user_data)

	#TODO: Check that username exists on github
	if response.status_code != 200:
		print('ERROR: Repos API failure')
	else:
		print('Repos Length', len(repos))
		for repo in repos:
			print('size:',repo['stargazers_count'])
			stars += repo['stargazers_count']


	return stars