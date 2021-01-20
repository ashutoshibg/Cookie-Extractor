from selenium import webdriver
import time
try:
    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    print("Created by Ashutosh Kumar "+"(ashutosh_ibg)")
    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*")
    print("Cookie Extractor")
    print("************************************************")
    web= input("Enter Website name (like- https://www.google.com): ")
    print("......Please Wait......")
    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    option = webdriver.FirefoxOptions()
    option.headless=True
    option.binary = binary
    driver = webdriver.Firefox(options=option, executable_path="geckodriver.exe")
    driver.get(web)
    a=driver.get_cookies()
    for x in a:
        print(x)
    time.sleep(2)
    driver.quit()
except Exception as a :
    print("Somthing Went Wrong"+"\n"+"Check Your internet Connect or Try again.")
