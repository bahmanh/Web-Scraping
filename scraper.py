from bs4 import BeautifulSoup
import requests

r = requests.get("https://sunspot.sdsu.edu/schedule/search?mode=search&period=20162&scheduleNumber=21002")
data = r.text
soup = BeautifulSoup(data, "html.parser")
seatData = soup.find_all("div",{"class": "sectionFieldSeats column"})[1].getText('\n').strip()

print seatData
