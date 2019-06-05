import requests
import json
fname = input("Enter your first name\n")
lname = input("Enter your last name\n")
req = requests.get("http://127.0.0.1:8081/process_get?first_name="+fname+"&last_name="+lname)
jsoned = json.loads(req.text)
first=jsoned.get("first")
last =jsoned.get("last")
print("Your full name reversed is: "+first+" "+last)