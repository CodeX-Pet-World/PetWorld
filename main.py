from flask import Flask, render_template, request, redirect,flash
import pymongo1
import os
app = Flask(__name__)
app.config["SECRET_KEY"] = 'hjhjdhghhjfjdjfjhfhu'
logged_in = False
email = ""


@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/logged_in")
def loggedin():
    return render_template("logged_in.html")


@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        data = request.form
        try:
            email = data.get("email")
            password = data.get("password")
            x = False #pymongo1.get_data(email, password)
            if x == True:
                global logged_in
                logged_in = True
                return redirect("http://127.0.0.1:5000/logged_in")
            elif x!=True:
                flash("Sorry Wrong Password Please Try Again", category='error')
                return render_template("login.html")
        except KeyError:
            flash("Sorry Wrong Password Please Try Again", category='error')
            return render_template("login.html", text="testing")
    elif request.method == "GET":
        return render_template("login.html")
        

@app.route("/diseases",methods=['GET','POST'])
def showw():
    if request.method == "GET":
        diseases = {"vomiting":"cancer,food poisoning,diarrhea","lumps":"skin cancer,tumor","fever":"pavrovirus,ear infection","itchiness":"ear infection,dermatitis,allergy","odor":"Mites,Urinary Tract Infection,Ear Infection"}
        #sym = ['vomiting', 'lumps', 'fever', 'itchiness', 'odor']
        return render_template("/diseases.html", sym = list(diseases.keys()))
    elif request.method == "POST":
        diseases = {"vomiting":"cancer,food poisoning,diarrhea","lumps":"skin cancer,tumor","fever":"pavrovirus,ear infection","itchiness":"ear infection,dermatitis,allergy","odor":"Mites,Urinary Tract Infection,Ear Infection"}
        pettype = request.form.get("pettype")
        symptoms = request.form.get("symptoms")
        #sym = ['vomiting', 'lumps', 'fever', 'itchiness', 'odor']
        return f"{pettype} has one of these diseases {diseases[symptoms]}"
@app.route("/signup",  methods=["GET", "POST"])
def signup():
    if (request.method =='GET'):
        return render_template('/signup.html')
    elif request.method=='POST':
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            conf_password = request.form.get("c_password")
            if password == conf_password:
                pymongo1.signup(username, email, password)
                return ("Successfully Logged in")
            else:
                flash("Sorry Passwords don't match",category='error')
                return render_template("/signup.html")

@app.route("/show")
def show():
    list_images = os.listdir("./static/")
    print(list_images)
    pymongo1.get_image(email,filename)
    return render_template("/image.html", image=list_images)
            
@app.route("/1")
def showww():
    diseases = [1,2,3,4,5,6,7,8] #{"vomiting":"cancer,food poisoning,diarrhea","lumps":"skin cancer,tumor","fever":"pavrovirus,ear infection","itchiness":"ear infection,dermatitis,allergy","odor":"Mites,Urinary Tract Infection,Ear Infection"}
    return render_template("./1.html", diseases=diseases) 
            
if __name__=="__main__":

    app.run(host='0.0.0.0', port='8000', debug='True')





        


