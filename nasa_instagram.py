from instabot import Bot
import os
import json
import requests
import time
import random  

'''
TODO add .gif condition 
'''

api_key = open("D:\\Python\\nasaeverday\\api_key.txt", "r").read() #windows
#api_key = open("/home/ec2-user/api_key.txt").read() #linux

passw = open("D:\\Python\\nasaeverday\\passw.txt", "r").read()
#passw = open("/home/ec2-user/passw.txt") #linux


url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
filename = "nasa_pic.jpg"

tags = ['#nasa','#space','#astro_photography','#astronauts','#planets','#deepsky','#astrography' ,'#telescope']

def download():
    req = requests.get(url)
    picture_url= req.json()['url']
    if 'jpg' not in picture_url:
        print("No image??")
    else:
        pic = requests.get(picture_url, allow_redirects=True)
        filename= os.path.abspath("D://Python//nasaeverday//nasa_pic.jpg")
        open(filename, 'wb').write(pic.content)
        print("Succesfully downloaded image")
        try:
            os.remove("D://Python//nasaeverday//nasa_pic.jpg.REMOVE_ME")
        except:
            pass

def upload_photo():
    bot=Bot()
    bot.login(username='everyday_nasa',password=passw)
    print("Logged in")
    
    while True:
        hashtags = random.choices(tags,k=3)
        hashtags_final = ' '.join(hashtags)
        #print(hashtags_final)
        try:
            bot.upload_photo("D://Python//nasaeverday//nasa_pic.jpg", caption=f"#everydaynasa {hashtags_final}")
            #time.sleep(timeout)
        
        except Exception as e:
            print(str(e))

        time.sleep(60)



if __name__ == '__main__':
    download()
    upload_photo()