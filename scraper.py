from bs4 import BeautifulSoup
import requests

r = requests.get("https://sunspot.sdsu.edu/schedule/search?mode=search&period=20162&admin_unit=R&abbrev=CS&number=560&suffix=&courseTitle=&scheduleNumber=&units=&instructor=&facility=&space=&meetingType=&startHours=&startMins=&endHours=&endMins=&remaining_seats_at_least=&ge=")

data = r.text
soup = BeautifulSoup(data, "html.parser")
seatData = soup.find_all("div",{"class": "sectionFieldSeats column"})[1].getText('\n').strip()

print seatData
