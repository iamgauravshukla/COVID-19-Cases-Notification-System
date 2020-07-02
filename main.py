from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:/Users/Gaurav/PycharmProjects/corona notification/icon.ico',
        timeout = 10
    )
def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    while True:
        caseData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(caseData, 'html.parser')

        caseStr = ""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            caseStr += tr.get_text()
        casesList = caseStr.split("\n\n")
        casesList = casesList[1:]

        states = ['Bihar','Uttar Pradesh','Delhi']
        for case in casesList[0:34]:
            dataList = case.split("\n")

            if dataList[1] in states:
                case_title = "Covid - 19 Cases"
                info = f"State : {dataList[1]} \nActive : {dataList[2] }  &  Cured : {dataList[3]} \nDeaths : {dataList[4]}\nTotal Cases : {dataList[5]}"
                notifyMe(case_title, info)
                import pyttsx3
                engine = pyttsx3.init()
                engine.say(info)
                engine.runAndWait()
                time.sleep(2)

        time.sleep(3600) # Program will runs in loop in every 1 hour