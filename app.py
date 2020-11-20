from flask import Flask
import csv
app = Flask(__name__)


@app.route('/')
def index():
    with open("index.html") as index_html:
        return index_html.read().replace("{{paragraphs}}", str(csvfile))


@app.route('/about')
def about():
    return "About"


with open('static/text.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)
