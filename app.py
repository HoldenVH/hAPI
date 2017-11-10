"""
Holden Higgins
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-10
"""
from flask import Flask, render_template
import urllib2, json

key="qzCQZVKqsIb7TpuGAqaFAVq25LIeqbu5KoS2HhDy"

app = Flask(__name__)

@app.route("/")
def fetch():
    request="https://api.nasa.gov/planetary/earth/imagery?lon=-74.01389389999997&lat=40.7180139&date=2017-5-10&api_key="
    "https://api.nasa.gov/planetary/apod?api_key="
    page=urllib2.urlopen(request+key)
    page=page.read()
#    page=page.decode("utf_8")
    pageDict=json.loads(page)
    #print page
    #print pageDict["url"]
    return render_template('template.html', url=pageDict["url"], description="a recent view of Stuyvesant High School and the surrounding neighborhood from the air using landsat 8")



app.debug=True
app.run()
#fetch()