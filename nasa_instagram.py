from instabot import Bot
import os
import json
import requests

api_key = open("D:\\Python\\nasaeverday\\api_key.txt", "r").read() #windows
#api_key = open("/home/ec2-user/api_key.txt").read() #linux

passw = open("D:\\Python\\nasaeverday\\passw.txt", "r").read()
#passw = open("/home/ec2-user/passw.txt") #linux


url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
filename = "nasa_pic.jpg"

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
    bot.upload_photo("D://Python//nasaeverday//nasa_pic.jpg", caption="#everydaynasa #nasa #space #planets #astro_photography #astronauts #deepsky #astrography #telescope")


if __name__ == '__main__':
    download()
    upload_photo()