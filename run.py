from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save_data', methods=['GET'])
def save_data():
    regno = request.args['regno']
    name= request.args['name']
    standard = request.args['league']
    goals = request.args['goals']
    yellow_cards = request.args['yellow_cards']
    red_cards = request.args['red_cards']
    print(regno,name,standard,goals,yellow_cards,red_cards)
    
    return redirect(url_for('home'))

app.run()