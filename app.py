from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

ass=[]
def urls(my_url):
    page = requests.get(my_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    js_test = soup.find_all('a', class_='item')
    global ass
    ass=[]
    temp=my_url.split('/')
    domain=''
    if(str(temp[0])=='https:' or str(temp[0])=='http:'):
        domain=temp[2]
    else:
        domain=temp[0]

    for i in js_test:
        if i.text!='..':
            i=str(i.get('href'))
            ass.append('https://'+domain+i.replace(' ','%20')+"?raw=true")

@app.route("/", methods = ['GET'])
def hello_world():
    return "Bello world"

@app.route('/index', methods=["GET"])
def scrape():
    url = request.args.get('url')
    urls(url)
    return render_template("index.html", l=ass)
