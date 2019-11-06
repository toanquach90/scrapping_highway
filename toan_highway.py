import csv
import requests, mechanize
from bs4 import BeautifulSoup

csvfile = open('highway.csv', 'a')
highway_writer = csv.writer(csvfile)

url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, 'html.parser')

main_table = soup.find('table', {'class': 'accidentOutput'})

row_list = main_table.find_all('tr')

for row in row_list:
	table_cells = row.find_all('td')

	output = []

	for cell in table_cells[1:]:
		output.append(cell.text.strip())
	highway_writer.writerow(output)
	