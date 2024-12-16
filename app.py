from flask import Flask, render_template

app = Flask(__name__,template_folder="templates")

@app.route('/')
def default():
    return render_template('index.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route('/home_1.html')
def home_1():
    return render_template("home_1.html")

@app.route('/home_2.html')
def home_2():
    return render_template("home_2.html")

@app.route('/home_3.html')
def home_3():
    return render_template("home_3.html")

@app.route('/search.html', methods=['POST'])
def search_html():
    return render_template("search.html")

@app.route("/goods.html")
def goods():
    return render_template("goods.html")

@app.route('/positions.html')
def positions():
    return render_template("positions.html")

@app.route('/user_1.html')
def user_1():
    return render_template("user_1.html")

@app.route('/user_2.html')
def user_2():
    return render_template("user_2.html")

@app.route('/user_3.html')
def user_3():
    return render_template("user_3.html")

@app.route('/user_4.html')
def user_4():
    return render_template("user_4.html")

if __name__ == '__main__':
    app.run(debug=True)