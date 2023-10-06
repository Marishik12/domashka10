import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
connection = sqlite3.connect("weather.db")
connection.execute(f"""CREATE TABLE IF NOT EXISTS temperature(date TEXT, time TEXT, temperature REAL)""")
page = requests.get(f"https://meteofor.com.ua/weather-kryvyi-rih-4978/")
soup = BeautifulSoup(page.content, 'html.parser')
temperature = soup.find(class_='today-temp').get_text()
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
connection.execute(f"INSERT INTO temperature (date,time,temperature) VALUES (?, ?, ?)", (date,time,temperature))
connection.commit()
connection.close()