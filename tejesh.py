from flask import Flask

app=Flask(__name__)


def hellof():
    return "Hello World!"
app.add_url_rule('/','hellof',hellof)

@app.route('/<name>')
def hi(name):
    return "Hello %s!" %name


if __name__=='__main__':
    app.run(debug=True)
