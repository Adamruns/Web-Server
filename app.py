from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    index_html = open("index.html")
    return index_html.read()


# if __name__ == '__main__':
#     port = 5000
#     app.run(host='0.0.0.0', port=port)
