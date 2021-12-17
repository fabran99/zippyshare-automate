from selenium import webdriver
import os
from datetime import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from constants import UPLOAD_URL, LINKS_NAMES_TEXTAREA_ID, SELECT_FILE_BUTTON_XPATH,START_UPLOAD_BUTTON_XPATH,\
    DOWNLOAD_BUTTON_ID

op = webdriver.ChromeOptions()
op.add_argument('--headless')
op.add_argument("log-level=3")
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          options=op
                          )


def upload_file(path):
    # Go to page
    driver.get(UPLOAD_URL)
    # find the file select button 
    select_file_button = driver.find_element_by_xpath(SELECT_FILE_BUTTON_XPATH)
    select_file_button.send_keys(os.getcwd()+path)
    # click in upload button
    start_upload_button = driver.find_element_by_xpath(START_UPLOAD_BUTTON_XPATH)
    start_upload_button.click()
    while True:
        sleep(10)
        # get current url
        current_url = driver.current_url
        print("URL actual: {}".format(current_url))
        # Check if the current url ends with "/upload"
        if current_url.endswith("/upload"):
            # get the element that contains the links
            links_names_textarea = driver.find_element_by_id(LINKS_NAMES_TEXTAREA_ID)
            # get the content of the textarea 
            links_names_textarea_content = links_names_textarea.get_attribute("value")
            # separate the text in lines, first line is filename and second line is link
            links_names_textarea_content_lines = links_names_textarea_content.split("\n")
            # get the link
            link = links_names_textarea_content_lines[1]
            # get the filename
            filename = links_names_textarea_content_lines[0]
            # generate and return dict with filename, link and upload date as a string in spanish format
            
            return {
                "filename": filename,
                "link": link,
                "upload_date": dt.now().strftime("%d/%m/%Y %H:%M:%S")
            }

# FOLDER = "./files/"
# files_and_links = []
# for file in os.listdir(FOLDER):
#     path = FOLDER + file
#     # upload the file and append the dict to files and links
#     print("Uploading {}".format(path))
#     files_and_links.append(upload_file(path))
#     print(files_and_links[-1])

# print("===========FINALIZADA LA SUBIDA ==============")
# print(files_and_links)


def download_file(url):
    # go to the url
    driver.get(url)
    # get the download button
    download_button = driver.find_element_by_id(DOWNLOAD_BUTTON_ID)
    # get href from the button
    download_button_href = download_button.get_attribute("href")
    # go to href 
    driver.get(download_button_href)
        

# def enable_download_in_headless_chrome( driver, download_dir):
#     # add missing support for chrome "send_command"  to selenium webdriver
#     driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

#     params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
#     command_result = driver.execute("send_command", params)

# enable_download_in_headless_chrome(driver, os.getcwd())
# files_dict = [{'filename': '1. Linear Search Algorithm.mp4', 'link': 'https://www120.zippyshare.com/v/x6NkK8E8/file.html', 'upload_date': '17/12/2021 02:07:28'}, 
# {'filename': '2. Linear Search Implementation in Python.mp4', 'link': 'https://www60.zippyshare.com/v/swXEMEwd/file.html', 'upload_date': '17/12/2021 02:08:50'}, 
# {'filename': '3. Recursion in Python.mp4', 'link': 'https://www8.zippyshare.com/v/xvmQsH7d/file.html', 'upload_date': '17/12/2021 02:10:09'}, 
# {'filename': '4. Binary Search Algorithm.mp4', 
# 'link': 'https://www34.zippyshare.com/v/cYZ7RXwz/file.html', 'upload_date': '17/12/2021 02:11:40'}, 
# {'filename': '5. Binary Search Implementation in Python.mp4', 'link': 'https://www108.zippyshare.com/v/DSgjTOpD/file.html', 'upload_date': '17/12/2021 02:12:55'}, 
# {'filename': '6. Binary Search using Recursion in Python.mp4', 'link': 'https://www93.zippyshare.com/v/swxldthU/file.html', 'upload_date': '17/12/2021 02:14:00'}]

# for file in files_dict:
#     download_file(file["link"])
#     print("Downloading {}".format(file["filename"]))
#     sleep(5)
   
# print("==========FINALIZADA LA BAJADA ===============")
