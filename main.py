import sqlite3
import time
import hashlib
from urllib.request import urlopen, Request
from urllib.parse import urlsplit, urlunsplit
import re

con = sqlite3.connect('C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
cursor = con.cursor()
cursor.execute("SELECT url FROM urls")
urls = cursor.fetchall()

x = 0
sep = "com"
while x < len(urls):
    split_url = urlsplit(str(urls[x]))
    # Use all the path except everything after the last '/'
    clean_path = "".join(split_url.path.rpartition("/")[: -1])
    stripped_text = clean_path.split(sep, 1)[0]
    print(f"clean {clean_path}")
    print(type(clean_path))
    urls[x] == stripped_text
    x += 1

# print(len(urls))
# for i in range(len(urls)):
#     count = 0
#     for j in range(len(urls)):
#         print(f"i {urls[i]}")
#         print(f"j {urls[j]}")
#         if urls[i] == urls[j]:
#             count += 1
#             print("boy")


# # setting the URL you want to monitor
# url = Request('https://leetcode.com/',
#               headers={'User-Agent': 'Mozilla/5.0'})
# # to perform a GET request and load the
# # content of the website and store it in a var
# response = urlopen(url).read()
#
# # to create the initial hash
# currentHash = hashlib.sha224(response).hexdigest()
# print("running")
# time.sleep(10)
# while True:
#     try:
#         # perform the get request and store it in a var
#         response = urlopen(url).read()
#
#         # create a hash
#         currentHash = hashlib.sha224(response).hexdigest()
#
#         # wait for 30 seconds
#         time.sleep(30)
#
#         # perform the get request
#         response = urlopen(url).read()
#
#         # create a new hash
#         newHash = hashlib.sha224(response).hexdigest()
#
#         # check if new hash is same as the previous hash
#         if newHash == currentHash:
#             continue
#
#         # if something changed in the hashes
#         else:
#             # notify
#             print("something changed")
#
#             # again read the website
#             response = urlopen(url).read()
#
#             # create a hash
#             currentHash = hashlib.sha224(response).hexdigest()
#
#             # wait for 30 seconds
#             time.sleep(30)
#             continue
#
#     # To handle exceptions
#     except Exception as e:
#         print("error")
