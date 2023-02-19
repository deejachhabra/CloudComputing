from flask import Flask, render_template, request
import csv 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/imgsearch")
def imgsearch():
    return render_template("imgsearch.html")

@app.route("/getImage", methods = ["POST", "GET"])
def getImage():
    path = ""
    if request.method == "POST":
        imgName = request.form["img"]
        Files = csv.DictReader(open('people.csv'))
        folder = "static/"
        for file in Files:
            if (imgName.title() == file['Name']):
                path = path+"static/" + file['Picture']
                print(path)
    if (path and path != folder):
        return render_template('getImage.html', path=path, message="Found it")
    else:
        return render_template('getImage.html', error="Better luck next time")

@app.route("/Salary")
def Salary():
    Files = csv.DictReader(open('people.csv'))
    path=[]
    for file in Files:
        if (file['Salary'] == '' or file['Salary'] == ' '):
            file['Salary'] = 99000
        if (int(file['Salary']) < 99000):
            if file['Picture'] != ' ':
                path.append('./static/'+ file['Picture'])
                print(path)
                print(int(file['Salary'])) 
    print(len(path))

    if path != '':
        return render_template('Salary.html', pic_path=path, message = 'We have it, dont worry')
    else:
        return render_template('Salary.html', error = 'Damn!')

@app.route('/addPicture')
def addPicture():
    return render_template('addPicture.html')

@app.route('/outputPic', methods=["POST","GET"])
def outputPic():
    if request.method == "POST":
        newF = request.files["new"]
        Files = csv.DictReader(open('people.csv'))
        folder = "static/"
        for Fil in Files:
            if newF.filename == Fil['Name']:
                return render_template('outputPic1.html', error = 'Damn!')
        newF.save(folder + newF.filename)
        return render_template('outputPic.html', name = newF.filename)

@app.route("/remove", methods = ["POST", "GET"])
def remove():
    pass



if __name__ == "__main__":
    app.run(debug=True)