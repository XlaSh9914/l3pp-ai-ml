from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

regions = ['Andheri West', 'Badlapur East', 'Ghansoli', 'Bhiwandi', 'Ambernath West', 
'Taloja', 'Ulwe', 'Badlapur West', 'Borivali East', 'Nala Sopara', 
'Palghar', 'Thane West', 'Parel', 'Kurla', 'Kalamboli', 'Panvel', 
'Boisar', 'Dahisar', 'Mira Road East', 'Karanjade', 'Kharghar', 
'Malad West', 'Girgaon', 'Vasai', 'Kandivali East', 'Borivali West', 
'Bandra West', 'Powai', 'Kalyan West', 'Mahim', 'Neral', 'Kalyan East', 
'Dombivali', 'Ghatkopar West', 'Mulund East', 'Kamothe', 'other', 
'Chembur', 'Andheri East', 'Ville Parle East', 'Kalwa', 'Khar', 
'Naigaon East', 'Nerul', 'Mulund West', 'Kanjurmarg', 'Santacruz East', 
'Airoli', 'Goregaon West', 'Santacruz West', 'Bhayandar East', 
'Seawoods', 'Karjat', 'Kandivali West', 'Sewri', 'Ambernath East', 
'Nilje Gaon', 'Khopoli', 'Titwala', 'Shil Phata', 'Vikhroli', 
'Goregaon East', 'Ghatkopar East', 'Bhandup West', 'Virar', 
'Koper Khairane', 'Dadar West', 'Anjurdive', 'Wadala', 'Taloje', 
'Dronagiri', 'Vashi', 'Lower Parel', 'Malad East', 'Colaba', 
'Nalasopara East', 'Sanpada', 'Sector 21 Kamothe', 'Kasheli', 
'Mazagaon', 'Bhandup East', 'Jogeshwari West', 'Belapur', 
'Jogeshwari East', 'Sion', 'Byculla', 'Bhayandar West', 'Worli', 
'Nahur East', 'Deonar', 'Ville Parle West', 'Dadar East', 'Agripada', 
'Virar West', 'Mazgaon', 'Dombivali East', 'Matunga', 'Juhu', 
'Bandra Kurla Complex', 'Bandra East', 'Prabhadevi', 'Mahalaxmi', 
'Ambarnath', 'Patlipada', 'Tardeo', 'Napeansea Road']

types = ['Apartment', 'Independent House', 'Studio Apartment', 'Villa']

with open('./2.Flask_site/model/house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template("index.html", regions=regions, types=types)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(features)
    print(features)
    print(prediction[0])
    return jsonify({'prediction': [prediction[0]]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)