from flask import Flask
import csv
app = Flask(__name__)


@app.route('/')
def index():
    with open('static/text.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        text = ""
        for row in reader:
            print(row)
            text = text + "<p>" + row[1] + "</p>\n"
    print(text)
    with open("index.html") as index_html:
        return index_html.read().replace("{{paragraphs}}", text)


@app.route('/about')
def about():
    with open('static/text.csv', newline='') as csvfile:
        reader = list(csv.reader(csvfile))

    with open("about.html") as about_html:
        template = about_html.read()
        template = template.replace("{{paragraph_1}}", reader[1][1])
        template = template.replace("{{paragraph_2}}", reader[2][1])
        return template


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)
