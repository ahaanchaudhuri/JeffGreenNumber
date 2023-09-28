import requests
from bs4 import BeautifulSoup
import sys
import json

player_links = []

with open('all_players.txt', 'r') as f:
	text = f.read()
	player_links = text.split(",")
player_links.pop()

URL = 'https://www.proballers.com/basketball/player/56756/qi-zhou/teammates'
base_URL = 'https://www.proballers.com'
teammates = '/teammates'
#REMOVE the 'Player Profile' at the start of the teammates web srape return

# {
# 	'name': 'Stephen Curry'
# 	'teammates': [{'Draymond Green': 'Golden State Warriors'}, {'Klay Thompson' : 'Golden State Warriors' ... ]
# }
with open('all_players_data.txt','w') as f:
	for player_link in player_links:
		curr_URL = base_URL + player_link + teammates
		#print(curr_URL)
		curr_player = {}
		r = requests.get(base_URL + player_link + teammates)
		soup = BeautifulSoup(r.content, 'html.parser')
		html = soup.findAll('tr', href=True)
		nameText = soup.find('div',{'class' : 'identity__name'}).text
		name = nameText.strip().replace('\nTeammates','')
		curr_player['teammates'] = {}
		curr_player['name'] = name
		for row in soup.findAll('tr'):
			parts = row.text.strip().split("\n")
			filtered = filter(lambda x: len(x.strip()) > 0 and x.strip()[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ", parts)
			mapped = list(map(lambda x: x.strip(), filtered))
			if mapped[0] != 'Player':
				curr_player['teammates'][mapped[0]] = mapped[1:]
		f.write(json.dumps(curr_player))


# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html.parser')
# html = soup.findAll('tr', href=True)
# nameText = soup.find('div',{'class' : 'identity__name'})
# print(nameText.text)
#print(soup.findAll('tr'))



# teammates = {}
# for row in soup.findAll('tr'):
# 	parts = row.text.strip().split("\n")
# 	filtered = filter(lambda x: len(x.strip()) > 0 and x.strip()[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ", parts)
# 	mapped = list(map(lambda x: x.strip(), filtered))
# 	if mapped[0] != 'Player':
# 		teammates[mapped[0]] = mapped[1:]
# print(teammates)
	#print(row.text.strip().split("\n"))
	#SPLIT BY \n and then find the ones that start w/ a capital letter
# for row in soup.findAll(href=True):
# 	for i in row.findAll('a',{'class': 'list-team-entry'},href=True):
# 		print(i)
# 	print("brreak")
	# if('/basketball/team' in row['href']):
	# 	print(row['title'])
