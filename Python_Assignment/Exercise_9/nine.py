'''
Below XML configuration file (config.xml) exists in current directory as the program. 
Write a program which reads API_URL and EMAIL_ID from below xml file. 
Take values of LATITUDE and LONGITUDE as a user input and replace them in API_URL. 
This URL works as HTTP get request. 
When proper values of latitude and longitude is provided it returns the json with information of that particular location.
Call this HTTP get request with the latitude and longitude values taken as an input from user. 
If request is successful then send an email to address configured 
	in EMAIL_ID with "<city> | <state> | <country>" information in the body and 
	subject as "Message from python script".

xml file's code as follow
<?xml version="1.0" encoding="UTF-8"?>

<CONFIG>

  <API_URL>http://maps.googleapis.com/maps/api/geocode/json?latlng=LATITUDE,LONGITUDE</API_URL>

  <EMAIL_ID>email_recipient@domain.com</EMAIL_ID>

</CONFIG>
'''
import xml.etree.ElementTree as ET
import urllib3
import smtplib
from smtplib import SMTPException
from geopy.geocoders import Nominatim
import json
#Fetching xml file
mytree=ET.parse('assignment9.xml')

#Getting latitude and longitude from user
user_latitude=input("Enter latitude value")
user_longitude=input("Enter longitude value")

#setting root_element to first tag of xml file
root_element=mytree.getroot()

#for loop to iterate in all tags to find the map API URL
for x in root_element.iter("API_URL"):
    #Set latitude and longitude values in URL 
    b=f"http://maps.googleapis.com/maps/api/geocode/json?latlng={user_latitude},{user_longitude}"
    x.text=b
    print(b)

#Writing new URL to XML file
mytree.write('assignment9.xml')

geolocator = Nominatim(user_agent="my-application")
location = geolocator.reverse(f"{user_latitude}, {user_longitude}")

data=[]
#assigning value to city state and country

city="City-   "+location.raw["address"]["state_district"]
state="State-   "+location.raw["address"]["state"]
country="Country-   "+location.raw["address"]["country"]
data.append(city)
data.append(state)
data.append(country)

with open('location.txt','w') as json_file:
    json.dump(data,json_file)
# print(location.raw)
with open('location.txt') as json_read:
    data=json.load(json_read)
    for i in data:
        print(i)
        
#Calling the URL
http = urllib3.PoolManager()
respone_code = http.request('GET', b)

#check if the area (i.e. given latitude and longitude) found or not
if(respone_code.status==200):
    #If response code is 200 it means that found
    for x in root_element.iter("EMAIL_ID"):
        user_mail_id=x.text
    user_mail_id=input("Enter your Email id")
    x.text=user_mail_id
    mytree.write('assignment9.xml')
    #Sender's mail
    from_user="ENTER YOUR MAIL ID"
    
    message = f"""Subject: Message from python script

    {city}
    {state}
    {country}   
    """
    #print is for if you want to see the message
    #print(message)
    
    #setting host(Gmail) and its port value(587 for Gmail)
    gmail_server = smtplib.SMTP('smtp.gmail.com',587)
    try:
        #gmail can't allow to send mail without encrypting so starttls method is written
        gmail_server.starttls()
        #Login to my gmail account to send mail
        gmail_server.login("ENTER YOUR MAIL ID", "ENTER YOUR MAIL PASSWORD")        
        #send mail method sends mail and it has three arguments 1. sender 2. receiver 3. message
        gmail_server.sendmail(from_user,user_mail_id,message)
        #Just for acknowledgement for user
        print("Sent Successfully")
    #While sending if any error occur then it prints below statement rather than exiting
    except SMTPException:
        print("Not sent")

#if response code is anything except 200  
else:
    print(respone_code.status)