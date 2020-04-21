
import sys
sys.path.insert(0, 'search_engine')
import controller
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def home():
  if request.method == 'POST':
    searchValue = request.form['value']
    results = controller.search(searchValue)
    return render_template('index.html', results=results)
  return render_template('index.html')


if __name__ == "__main__":
    app.run()
