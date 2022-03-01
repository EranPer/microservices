from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


@app.route('/steve', methods=['POST', 'GET'])
def steve():
    if request.method == "POST":
        if request.form['submit_button'] == 'A special gift for Mike':
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)
        elif request.form['submit_button'] == 'Get Message':
            data = requests.get('http://mary-service:5051').json()
            flash(str(data), "green")
            return redirect(url_for('steve'))
        else:
            pass
    return render_template('steve_service.html')


if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")