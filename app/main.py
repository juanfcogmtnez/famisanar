from flask import Flask, render_template, jsonify, url_for, send_file

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
