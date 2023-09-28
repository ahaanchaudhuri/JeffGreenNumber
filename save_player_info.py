import requests
from bs4 import BeautifulSoup
import sys




player_links = []
URL = 'https://www.proballers.com/basketball/league/3/nba/players/'
start_year = 1949
end_year = 2021
file_name = 'all_players.txt'
for i in range(end_year - start_year):
	curr_URL = URL + str(start_year + i)	
	r = requests.get(curr_URL)
	soup = BeautifulSoup(r.content,'html.parser')
	for row in soup.findAll('a', {'class': 'list-player-entry'}):
		ref = row['href']
		if not ref in player_links:
			player_links.append(ref)
print(player_links)
with open(file_name,'w') as f:
	for i in player_links:
		f.write(i)
		f.write(",")
