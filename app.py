from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/math',methods=['POST'])
def result():
    if request.method == 'POST':
        opt = request.form['operations']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
       
        if opt == 'add':
            result = num1+num2
        if opt == 'subtraction':
            result = num1+num2
        if opt == 'multiplication':
            result = num1+num2
        if opt == 'division':
            result = num1/num2        
    return render_template('result.html',result=result)


@app.route('/post-man',methods=['POST'])
def result1():
    if request.method == 'POST':
        opt = request.json['operations']
        num1 = request.json['num1']
        num2 = request.json['num2']
        if opt == 'add':
            result = num1+num2
        if opt == 'subtraction':
            result = num1-num2
        if opt == 'multiplication':
            result = num1*num2
        if opt == 'division':
            result = num1/num2        
    return jsonify(result)
        
# if __name__ == '__main__':
#     app.run(debug=True)
