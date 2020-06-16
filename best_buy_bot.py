import re
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.firefox.options import Options
from playsound import playsound

# Ring Fit which is sold out :'(
url = 'https://www.bestbuy.com/site/ring-fit-adventure-nintendo-switch/6352149.p?skuId=6352149A'

# # Zephyrus G14 is in stock
# url = "https://www.bestbuy.com/site/asus-rog-zephyrus-g14-14-gaming-laptop-amd-ryzen-9-16gb-memory-nvidia-geforce-rtx-2060-max-q-1tb-ssd-moonlight-white/6403816.p?skuId=6403816"

p = re.compile("Sold Out")

# Start firefox without the browser popping up -- "headless".
fireFoxOptions = Options()
fireFoxOptions.headless = True

duration = 1  # seconds
freq = 440  # Hz

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)

while True:
  try:
    driver.get(url)
  except TimeoutException:
    continue
  html = str(driver.page_source)
  
  
  if p.search(html):
      print("Sold out")
  else:
      print("In stock!!!")
      # os.system('say "In stock."')
      while True:
        playsound("/Users/mitchlin/Downloads/friends.mp3")
