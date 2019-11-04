import requests, mechanize
from bs4 import BeautifulSoup

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, 'html.parser')

#Dig through the HTML - updated on Nov 4
main_table = soup.find('table', {'class': 'accidentOutput'})

row_list = main_table.find_all('tr')

for row in row_list:

	table_cells = row.find_all('td')

	output = []

	for cell in table_cells:
		print(cell.text)

		#When running the file in Terminal, all results are shown in Terminal window