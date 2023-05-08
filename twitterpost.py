import tweepy
import openpyxl
import random

#Genarate tree and consecutive numbers from 1-143.
numx = random.randint(1,143)
numy = numx + 1
numz = numx + 2
num1 = str(numx)
num2 = str(numy)
num3 = str(numz)


#Excell stuffs to get the lyrcis of the tree rows
book = openpyxl.load_workbook("Letras.xlsx")
sheet = book.active
a1 = str(sheet["A" + num1].value)
a2 = str(sheet["A" + num2].value)
a3 = str(sheet["A" + num3].value)

#Concatenate the tree rows into one string call quote
quote = a1+"\n"+a2+"\n"+a3


#Access to Twitter using API V2 authentication
client = tweepy.Client(consumer_key='API KEY',
                       consumer_secret='API KEY SECRET',
                       access_token='ACCESS TOKEN',
                       access_token_secret='ACCESS TOKEN SECRET')

#Post the quote string to Twitter Status
response = client.create_tweet(text=quote)

