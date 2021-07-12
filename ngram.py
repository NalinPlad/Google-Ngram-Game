import requests
import json
import csv
import urllib
import random


print("Welcome to the Google Ngram Game! \n")
print("*--------------------------------* \n")
print("HOW TO PLAY----------------------* \n")
print("When prompted, enter [1] or [2]  \n based on which of the two \n you think is used more in \n literature.")
print("ABOUT----------------------------* \n")
print("Google Ngram is a place where you \n can check the frequency of \n words used in writing. You \n can use Ngram at \n https://books.google.com/ngrams/")
smoothing = 10

words = []
with open('nouns.csv', newline='') as csvfile:
     nouns = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in nouns:
         words.append(''.join(row))



def get_word():

    word = random.choice(words)



    # print(f"Data for {word}")
    url = f"https://books.google.com/ngrams/json?content={word}&year_start=2018&year_end=2019&corpus=26&smoothing={smoothing}"

    r = urllib.request.urlopen(url)
    data = r.read().decode(r.info().get_param('charset') or 'utf-8')
    data1 = data.split(',')
    data2 = ''.join(data1[4])
    data3 = float(data2[0:-3])
    data4 = format(data3, 'f')
    return data4,word

while True:
    word1 = get_word()
    word2 = get_word()

    print("\n *-----------Google Ngram Game------------* \n")

    user_input = input(f"Which word do think is used more? {word1[1]} [1] or {word2[1]} [2]  (Type 1 or 2): ")

    if user_input is not '1' and user_input is not '2':
        print("Please enter either [1] or [2]!")
        continue
    elif user_input == '1' and word1[0] > word2[0]:
        print("Correct!")
    else:
        print("Incorrect!")
