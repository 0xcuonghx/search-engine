
import sys
sys.path.insert(0, 'search_engine')
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
    searchValue = request.args.get("page")
  results = controller.search(searchValue, page)
  return render_template('index.html', results=results, searchValue=searchValue, page=page)

if __name__ == "__main__":
    app.run()
