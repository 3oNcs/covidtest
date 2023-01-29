from flask import Flask
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST', 'DELETE'])
def index():
    if request.method != "POST":
        return render_template("main.html",data="No Date Selected")
    date = request.form['text']
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
    querystring = {"date":date}
    headers = {
        "X-RapidAPI-Key": "8ee6867cfamsh5fff54cd0f7593dp13a35cjsndc0b4bb45c9c",
        "X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    if "error" in response.json():
        return render_template("main.html",data="Format Error: Please make sure to enter the date in YYYY-MM-DD format.")
    data = response.json()["data"]
    pass
    return render_template("main.html",data=data)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8080)