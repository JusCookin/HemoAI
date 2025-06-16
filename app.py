from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/results', methods = ["POST"])
def prediction():
    
    Name = request.form["name"]
    Hemo = request.form["hb"]
    Gender = request.form["gender"]
    MCH = request.form["mch"]
    MCHC = request.form["mchc"]
    MCV = request.form["mcv"]
     
    if Gender == "Male":
        g = 0
    else:
        g = 1
    x_test = [[g,float(Hemo),float(MCH),float(MCHC),float(MCV)]]
    print(x_test)
    
    p = np.array(x_test)
    p = p.astype(np.float32)
    
    prediction = model.predict(p)
    
    
    if (prediction == 0):
        text = "You don't have Anemic Disease"
    else:
        text = "You have Anemic Disease"
        
    
    return render_template("results.html",f = Name, e = Gender, a = Hemo, b = MCH, c = MCHC, d = MCV, predicted_res = "Based on the Blood Report Data: " + str(text)) 

    
if __name__ == "__main__":
    app.run(debug = True)
