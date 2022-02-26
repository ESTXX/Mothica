## Web scrape NASA Spaceflight for upcoming launches.
import requests
from bs4 import BeautifulSoup


url = 'https://nextspaceflight.com/launches/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

def main():
    flights = []
    rows = soup.find_all('div', class_='mdl-cell mdl-cell--6-col')
    for row in rows:
        lsp = row.find('div', class_="mdl-card__title-text").text.strip()
        rocket_and_payload = row.find('h5', class_="header-style").text.strip()
        date_and_time = row.find('div', class_="mdl-card__supporting-text").next.strip()
        launch_site = row.find('div', class_="mdl-card__supporting-text").br.next.strip()
        flights.append([lsp, rocket_and_payload, date_and_time, launch_site])
    return flights

if __name__ == '__main__':
    all_flights = main()
    for flight in all_flights:
        for i in flight:
            print(i)
        print('')
        

        
