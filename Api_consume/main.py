from flask import Flask, render_template, request
import requests

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
     return render_template('index.html')
    if request.form['search']:
        url= "https://api.giphy.com/v1/gifs/trending?api_key=gNjApqTwXJ6mOoJt0Eg57TnvyRGSazsB&limit=10&q=cat" + request.form['search']
        giphy= requests.get(url)
        datagiphy=giphy.json()
        return render_template('index.html', data= datagiphy['data'])
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4000)