from flask import Flask, render_template, request, url_for
import os
import csv



app = Flask(__name__)
app.config['FOLDER'] = 'static'



@app.route('/')
def home():
    full_filename = os.path.join(app.config['FOLDER'], 'm-1.jpg')
    return render_template("home.html", user_image=full_filename)

@app.route('/show')
def show():  
    return render_template('show.html') 

@app.route('/show1', methods=["POST"])
def show1():
    if request.method == "POST":
        data = csv.DictReader(open('data-1.csv'))
        name=[]
        pic = []
        cla = []
        income = []
        comments = []
        # no =[]
        count = 0
        for d in data:
            if d['picture'] == "" or d["picture"] == " " or d['picture'] == ",":
                pic.append("no picture found")
            else:
                pic.append(os.path.join(app.config['FOLDER'], d['picture']))
            name.append(d['name'])
            cla.append(d['class'])
            income.append(d['income'])
            comments.append(d['comments'])
            count+=1
    lenName = len(name)
    if count != 0:
        return render_template('show1.html', name=name,pic = pic,cla = cla, income=income, comments=comments, len=count, message = "Result")
    else:
        return render_template('show1.html', error="No data found")

@app.route('/getRange')
def getRange():
    return render_template('getRange.html')

@app.route('/result', methods=["POST", "GET"])
def result():
    if request.method == "POST":
        low = int(request.form['low'])
        high = int(request.form['high'])
        dataFile = csv.DictReader(open('data-1.csv'))
        r_name=[]
        r_pic = []
        r_cla = []
        r_income = []
        r_comments = []
        count = 0
        for d in dataFile:
            if (d['income'] == "" ) or (d['income'] == " ") :
                continue
            if (low <= int(d['income']) <= high) :
                if d['picture'] == "" or d["picture"] == " " or d['picture'] == ",":
                    r_pic.append("no picture found")
                else:
                    r_pic.append(os.path.join(app.config['FOLDER'], d['picture']))
                r_name.append(d['name'])
                r_cla.append(d['class'])
                r_income.append(d['income'])
                r_comments.append(d['comments'])
                count+=1
            else:
                continue                
    lenName = len(r_name)
    if count != 0:
        return render_template('result.html', name=r_name,pic = r_pic,cla = r_cla, income=r_income, comments=r_comments, len=count,low = low, high=high, message = "Result")
    else:
        return render_template('result.html', error="No data found")

@app.route("/nameC", methods = ["GET"])
def nameC():
    return render_template("nameC.html")

@app.route("/nameResult", methods = ["POST" "GET"])
def nameResult():
    if request.method == "POST":
        nam = str(request.form['fname'])
        Comm = str(request.form['fcomm'])
        Inc = str(request.form['fincome'])
    data = csv.DictReader(open('data-1.csv'))
    for da in data:
        if da['name'] == nam:
            da['comments'] = Comm
            da['income'] = Inc
            return render_template("nameResult.html", message = "success")
    return render_template("nameResult.html", message = "error")
   



    



if __name__ == "__main__":
    app.run(debug = "True")