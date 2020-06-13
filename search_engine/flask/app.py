
import sys
sys.path.insert(1, 'C:\IR-IT4853\search_engine')
import controller
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  searchValue = ''
  page = 1
  if request.args.get("value"):
    searchValue = request.args.get("value")
  if request.args.get("page"):
    page = request.args.get("page")
    page = int(page)
  rs = controller.search(searchValue, page)
  print(searchValue)
  return render_template('index.html', results=rs["results"], numFound=rs["numFound"], searchValue=searchValue, page=page)

if __name__ == "__main__":
    # app.run()
    app.run(host='192.168.0.124')
