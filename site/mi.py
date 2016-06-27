from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app) # enable bootstrap

@app.route("/")
def index():
	return render_template('index.html')


@app.route('/spider')
def spider():
	return render_template('spider.html')

@app.route('/analysis')
def analysis():
	return render_template('analysis.html')

if __name__ == "__main__":
	app.run(debug=True)