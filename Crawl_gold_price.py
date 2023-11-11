import re
from selenium import webdriver
from bs4 import BeautifulSoup

# create a new instance of the Chrome driver
driver = webdriver.Chrome()

# load the webpage
driver.get("https://webgia.com/gia-vang/sjc/bieu-do-3-thang.html")

# get the HTML source code
html = driver.page_source

# parse the HTML source code using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# find the JavaScript variable containing the data
script = soup.find("script", text=re.compile("var seriesOptions ="))

# extract the data from the JavaScript variable
match = re.search(r"data:(\[\[.*?\]\])", script.text)
data = match.group(1)

# print the data
print(data)
# quit the driver
driver.quit()