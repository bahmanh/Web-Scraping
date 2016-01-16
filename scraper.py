from bs4 import BeautifulSoup
import requests
import time

def getData():

    r = requests.get("https://sunspot.sdsu.edu/schedule/search?mode=search&period=20162&scheduleNumber=21002")
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    className = soup.find_all("a", {"href": "sectiondetails?scheduleNumber=21002&period=20162&admin_unit=R"})[0].text
    seatData = soup.find_all("div",{"class": "sectionFieldSeats column"})[1].getText('\n').strip()

   # print "=========================="+'\n'
   # print className
   # print seatData + '\n'
    availableSeats = seatData.split('/')
    print availableSeats[0]

def freshData():
    while True:
        getData()
        time.sleep(3)

if __name__ == '__main__':
    freshData()
