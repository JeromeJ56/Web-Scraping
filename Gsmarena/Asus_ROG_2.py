# Importing Required Libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

# By downloading webdriver for FireFox Browser and placed it in the working directory you can lanuch firefox session
# You can visit Following url for additional Information
# https://pypi.org/project/selenium/
driver = webdriver.Firefox()
driver.get("https://www.gsmarena.com/")
time.sleep(3)
# From Home page of GSMArena navigate to Asus phones by clicking the Asus button by using selenium
element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/aside/div[1]/ul/li[19]/a')
element.click()
time.sleep(3)
# From Asus Home page to Navigate the Phone model page by clicking the ROG Phone 2
button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/ul/li[1]/a/img")
button.click()
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep(3)
mobile_os = soup.find('td', {'data-spec': 'os'}).text.replace(',', '')
chipset = soup.find('td', {'data-spec': 'chipset'}).text
cpu = soup.find('td', {'data-spec': 'cpu'}).text
gpu = soup.find('td', {'data-spec': 'gpu'}).text
technology = soup.find('a', {'class': 'link-network-detail'}).text
speed = soup.find('td', {'data-spec': 'speed'}).text.replace(',', '')
announced = soup.find('td', {'data-spec': 'year'}).text.replace(',', '')
dimensinos = soup.find('td', {'data-spec': 'dimensions'}).text
weight = soup.find('td', {'data-spec': 'weight'}).text
build = soup.find('td', {'data-spec': 'build'}).text.replace(',', '')
sim = soup.find('td', {'data-spec': 'sim'}).text.replace(',', '')
display = soup.find('td', {'data-spec': 'displaytype'}).text.replace(',', '')
size = soup.find('td', {'data-spec': 'displaysize'}).text.replace(',', '')
resolution = soup.find('td', {'data-spec': 'displayresolution'}).text.replace(',', '')
protection = soup.find('td', {'data-spec': 'displayprotection'}).text
memory_card = soup.find('td', {'data-spec': 'memoryslot'}).text
internal = soup.find('td', {'data-spec': 'internalmemory'}).text.replace(',', '')
camera = soup.find('td', {'data-spec': 'cam1modules'}).text.replace(',', '').replace('\r', '').replace('\n', '')
camera_features = soup.find('td', {'data-spec': 'cam1features'}).text.replace(',', '')
camera_video = soup.find('td', {'data-spec': 'cam1video'}).text.replace(',', '')
front_camera = soup.find('td', {'data-spec': 'cam2modules'}).text.replace(',', '')
front_camera_features = soup.find('td', {'data-spec': 'cam2features'}).text.replace(',', '')
front_camera_video = soup.find('td', {'data-spec': 'cam2video'}).text.replace(',', '')
wlan = soup.find('td', {'data-spec': 'wlan'}).text.replace(',', '')
bluetooth = soup.find('td', {'data-spec': 'bluetooth'}).text.replace(',', '')
gps = soup.find('td', {'data-spec': 'gps'}).text.replace(',', '')
nfc = soup.find('td', {'data-spec': 'nfc'}).text
radio = soup.find('td', {'data-spec': 'radio'}).text
usb = soup.find('td', {'data-spec': 'usb'}).text.replace(',', '')
sensors = soup.find('td', {'data-spec': 'sensors'}).text.replace(',', '')
battery = soup.find('td', {'data-spec': "batdescription1"}).text
colors = soup.find('td', {'data-spec': "colors"}).text.replace(',', '')
time.sleep(3)
driver.close()

with open('Asus_ROG.csv', 'w', encoding='utf-8') as f:
    f.write("Operating System," + str(mobile_os) + "\n")
    f.write("Chipset," + str(chipset) + "\n")
    f.write("CPU," + str(cpu) + "\n")
    f.write("GPU," + str(gpu) + "\n")
    f.write("Technology," + str(technology) + "\n")
    f.write("Speed," + str(speed) + "\n")
    f.write("Date Of Announce," + str(announced) + "\n")
    f.write("Dimenstion," + str(dimensinos) + "\n")
    f.write("Weight," + str(weight) + "\n")
    f.write("Build," + str(build) + "\n")
    f.write("SIM Slot," + str(sim) + "\n")
    f.write("Display," + str(display) + "\n")
    f.write("Display Size," + str(size) + "\n")
    f.write("Display Resolution," + str(resolution) + "\n")
    f.write("Display Protection," + str(protection) + "\n")
    f.write("Memory Slot," + str(memory_card) + "\n")
    f.write("Internal Memory," + str(internal) + "\n")
    f.write("Rear Camera," + str(camera) + "\n")
    f.write("Rear Camera Features," + str(camera_features) + "\n")
    f.write("Rear Camera Video," + str(camera_video) + "\n")
    f.write("Front Camera," + str(front_camera) + "\n")
    f.write("Front Camera Features," + str(front_camera_features) + "\n")
    f.write("Front Camera Video," + str(front_camera_video) + "\n")
    f.write("WLAN," + str(wlan) + "\n")
    f.write("Bluetooth," + str(bluetooth) + "\n")
    f.write("GPS," + str(gps) + "\n")
    f.write("NFC," + str(nfc) + "\n")
    f.write("Radio," + str(radio) + "\n")
    f.write("USB," + str(usb) + "\n")
    f.write("Sensors," + str(sensors) + "\n")
    f.write("Battery," + str(battery) + "\n")
    f.write("Colors," + str(colors) + "\n")

f.close()
