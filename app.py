from flask import Flask,redirect,request
from flask.templating import render_template

app=Flask(__name__)
medicines=[
    {"Id":1,"Name":"Med1","For":"Cough/Cold","cost":"20","img":"../static/med1.svg","status":"ADD","qty":1},
    {"Id":2,"Name":"Med2","For":"Acidity","cost":"25","img":"../static/med2.svg","status":"ADD","qty":1},
    {"Id":3,"Name":"Med3","For":"Headache","cost":"20","img":"../static/med3.svg","status":"ADD","qty":1},
    {"Id":4,"Name":"Med4","For":"Acidity","cost":"25","img":"../static/med2.svg","status":"ADD","qty":1},
    {"Id":5,"Name":"Med5","For":"Cough/Cold","cost":"20","img":"../static/med1.svg","status":"ADD","qty":1},
    {"Id":6,"Name":"Med6","For":"Headache","cost":"20","img":"../static/med3.svg","status":"ADD","qty":1},
    {"Id":7,"Name":"Med7","For":"Allergy","cost":"80","img":"../static/med4.svg","status":"ADD","qty":1},
    {"Id":8,"Name":"Med8","For":"Headache","cost":"20","img":"../static/med3.svg","status":"ADD","qty":1},
    {"Id":9,"Name":"Med9","For":"Acidity","cost":"25","img":"../static/med2.svg","status":"ADD","qty":1},
    {"Id":10,"Name":"Med10","For":"Acidity","cost":"25","img":"../static/med2.svg","status":"ADD","qty":1},
    {"Id":11,"Name":"Med11","For":"Headache","cost":"20","img":"../static/med3.svg","status":"ADD","qty":1},
    {"Id":12,"Name":"Med12","For":"Cough/Cold","cost":"20","img":"../static/med1.svg","status":"ADD","qty":1},
]
cart_obj=[]
hospitals=[
    {"Id":1,"Name":"ABC Hospital","Address":"25, Some street, Some Area, Some City","PinCode":781001},
    {"Id":2,"Name":"BCD Hospital","Address":"26, Some street, Some Area, Some City","PinCode":781002},
    {"Id":3,"Name":"CDE Hospital","Address":"27, Some street, Some Area, Some City","PinCode":781003},
    {"Id":4,"Name":"DEF Hospital","Address":"28, Some street, Some Area, Some City","PinCode":781004},
    {"Id":5,"Name":"EFG Hospital","Address":"29, Some street, Some Area, Some City","PinCode":781005},
    {"Id":6,"Name":"FGH Hospital","Address":"30, Some street, Some Area, Some City","PinCode":781006},
    {"Id":7,"Name":"GHI Hospital","Address":"31, Some street, Some Area, Some City","PinCode":781007},
    {"Id":8,"Name":"HIJ Hospital","Address":"32, Some street, Some Area, Some City","PinCode":781008},
    {"Id":9,"Name":"IJK Hospital","Address":"33, Some street, Some Area, Some City","PinCode":781009},
    {"Id":10,"Name":"JKL Hospital","Address":"34, Some street, Some Area, Some City","PinCode":781010},
    {"Id":11,"Name":"KLM Hospital","Address":"35, Some street, Some Area, Some City","PinCode":781011},
    {"Id":12,"Name":"LMN Hospital","Address":"36, Some street, Some Area, Some City","PinCode":781012}   
]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/order')
def order():
    return render_template('order.html',medicines=medicines)
@app.route('/hospitals')
def hospital():
    return render_template('hospital.html',hospitals=hospitals)
@app.route('/cart')
def cart():
    return render_template('cart.html',cart=cart_obj)
@app.route('/added/<int:i>',methods=['POST'])
def added(i):
    if(medicines[i-1]["status"]=="ADD"):
        medicines[i-1]["status"]="REMOVE"
        medicines[i-1]["qty"]=request.form.get("qty")
        cart_obj.append(medicines[i-1])
        print(cart_obj)
    elif(medicines[i-1]["status"]=="REMOVE"):
        for data in cart_obj:
            if(data['Id']==i):
                cart_obj.remove(data)
        medicines[i-1]["status"]="ADD"
        medicines[i-1]["qty"]="1"
        print(cart_obj)
    return render_template('order.html',medicines=medicines)
@app.route('/address')
def address():
    return render_template('address.html')
@app.route('/final',methods=['POST'])
def final():
    details={
        "Name":request.form.get("name"),
        "Country":request.form.get("country"),
        "phno":request.form.get("phno"),
        "email":request.form.get("email"),
        "address":request.form.get("address"),
        "mode":request.form.get("mode")
    }

    if(details["Name"]!=""):
        if(details["Country"]!=""):
            if(details["phno"]!=""):
                if(details["email"]!=""):
                    if(details["address"]!=""):
                        if(details["mode"]!=""):
                            total_cost=0
                            for data in cart_obj:
                                total_cost+=float(data['cost'])*float(data['qty'])
                            return render_template('final.html',details=details,cart=cart_obj,total_cost=total_cost)
    else:
        return redirect('/address')
if(__name__=='__main__'):
    app.run(debug=True)