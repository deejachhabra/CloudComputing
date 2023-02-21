from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

server = 'server-ass02.database.windows.net'
database = 'db'
username = 'chhab'
password = 'Dollyash@7'
driver= '{ODBC Driver 17 for SQL Server}'

# conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
# print(conn)
try:
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
    print("\n===============================Connected===========================")
    cursor = conn.cursor()
except Exception as e:
    print(e)
    print("\n**********************unable to connect************************")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/greaterhalf")
def greaterhalf():

    cursor.execute("select * from [all_month] where mag > 5.0")
    rows = cursor.fetchall()
    num = len(rows)
    print("greaterhalf", num)
    return render_template("greaterhalf.html", rows = rows, num=num)

@app.route("/date")
def date():
    return render_template("date.html")

@app.route("/duration", methods=["POST", "GET"])
def duration():
    if request.method == "POST":
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        low = request.form['low']
        high = request.form['high']
        print(startDate)
        print(type(startDate), type(endDate))

        query = "select place, mag, latitude, longitude, [date] = CONVERT(date, [time]) from all_month where CONVERT(date, [time]) between ? and ? and MAG >= "+str(low)+" AND MAG < "+str(high)+" "
        cursor.execute(query, (startDate, endDate))
        rows = cursor.fetchall()
        num = len(rows)
        print("duration", num)
    return render_template("duration.html", rows=rows, num=num)

@app.route("/getinput")
def getinput():
    return render_template("getinput.html")

@app.route("/equakes", methods = ["POST", "GET"])
def equakes():
    if(request.method == "POST"):
        Lat = float(request.form['latitude'])
        Lon = float(request.form['longitude'])
        range = float(request.form['range'])
        print("Lat", Lat)
        print("Lon", Lon)
        print("r", range)
        lat1 = Lat-(range/111)
        lat2 = Lat+(range/111)
        long1 = Lon-(range/111)
        long2 = Lon+(range/111)
        query = "SELECT * from [all_month] where latitude >= "+str(lat1)+" and latitude < "+str(lat2)+" and longitude >= "+str(long1)+" and longitude < "+str(long2)+"" 
        cursor.execute(query)
        rows = cursor.fetchall()
        num = len(rows)
        print("n", num)
    return render_template("equakes.html", rows = rows, num=num )

# @app.route("/nightinp")
# def nightinp():
#     return render_template("nightinp.html")

@app.route("/mag")
def mag():
    return render_template("mag.html")

@app.route("/result", methods = ["POST" , "GET"])
def result():
    if request.method == "POST":
        mg = str(request.form['mg'])
        print("enter", mg)
        t1 = "6:00:00:00"
        t2= "18:00:00:00"
        t3 = "23:59:00:00"
        t4 = "00:00:00:00"
        query1 = "select count(*) as count from [all_month] where CONVERT(time, [time]) between ? and ? and mag > ?"
        cursor.execute(query1, (t1, t2, mg))
        num1 = cursor.fetchall()
        query2 = "select count(*) as count from [all_month] where (CONVERT(time, [time]) between ? and ? or CONVERT(time, [time]) between ? and ?)  and mag > ?"
        cursor.execute(query2, (t2, t3, t4, t1, mg))
        num2 = cursor.fetchall()
        return render_template("result.html", num1 = num1[0][0], num2 = num2[0][0])


# @app.route("/night", methods = ["POST", "GET"])
# def night():
#     if request.method == "POST":
#         times1 = request.form['times']
#         times2 = request.form['etimes']

#         print("time input", times1, times2)
#         times1 = times1 + ":00:00"
#         times2 = times2 + ":00:00"
#         print("times again", times1, times2)
#         # query1 = "SELECT (cast(DATEPART(hour, [time]) as varchar) + ':' + cast(DATEPART(minute, [time]) as varchar)) from [all_month] as t where t >= "+"23:00"+" and t <= "+"05:00"+""
#         # cursor.execute(query1)
#         query = "select place, mag, latitude, longitude,[date] = CONVERT(date, [time]),  [time] = CONVERT(time, [time]) from [all_month] where CONVERT(time, [time]) between ? and ? and mag >= 4.0"
#         cursor.execute(query, (times1, times2))
#         rows = cursor.fetchall()
#         num = len(rows)
#         print("no", num)
#     return render_template("night.html", rows = rows, num=num)

@app.route("/clusters")
def clusters():
    return render_template("clusters.html")

@app.route("/clusters_out", methods = ["POST", "GET"])
def clusters_out():
    if request.method == "POST":
        names = str(request.form['clusters'])
        print("Hello")
        print("names", names)
        query = "select place, mag, latitude, longitude, updated from [all_month] where TRIM(SUBSTRING(PLACE, CHARINDEX(',', place)+1, len(place))) = ?"
        cursor.execute(query, (names))
        rows = cursor.fetchall()
        num = len(rows)
    return render_template("clusters_out.html", rows = rows, num=num)

@app.route("/net")
def net():
    return render_template("net.html")

@app.route("/netval", methods = ["POST", "GET"])
def netval():
    if request.method == "POST":
        loc = str(request.form['loc'])
        mgs = str(request.form['mgs'])
        q = "Update [all_month] set mag = ? where locationSource = ? "
        cursor.execute(q, (mgs, loc))
        q2 = "select place, mag, latitude, longitude, locationSource from [all_month] where locationSource = ?" 
        cursor.execute(q2, (loc))
        rows = cursor.fetchall()
        num = len(rows)
        print(num)
    return render_template("netval.html", rows = rows, num=num)

if __name__ == "__main__":
    app.run(debug = True)