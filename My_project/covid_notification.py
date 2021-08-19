from plyer import notification
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def notifyMe(title, message):
    '''Function for notification
    Its take title and message as argument and give notification '''
    notification.notify( title = title,
                         message= message,
                         app_icon = "icon.ico",   #icon path (in this case it is in the folder of program)
                         timeout = 20)


if __name__ == '__main__':
    while True:                          #To run infinite loop
        option = webdriver.ChromeOptions()
        option.add_argument('headless')     #hide the chrome

        url = 'https://www.mohfw.gov.in/'
        driver = webdriver.Chrome(executable_path='C:\\Pycharm\\chromedriver.exe', options=option)  #path should be where you have downloaded the chromedriver
        driver.get(url)         #because its a dynamic page we are using selenium
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        states = ['Delhi', 'Himachal Pradesh', 'Chandigarh']   #States name whose data we want
        for data in soup.findAll('tbody'):
            for tr in data.findAll('tr')[:37]:
                list = [td for td in tr.stripped_strings]
                if list[1] in states:
                    ntitle = "Covid 19 Cases Stats"
                    ntext = f"State {list[1]}\nActive:{list[2]}\nCured:{list[4]}\nDeaths:{list[6]}"
                    notifyMe(ntitle, ntext) #calling notification function
                    time.sleep(2)
        time.sleep(3600)  #Gives notification in every 1 hour


