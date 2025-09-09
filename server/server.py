from flask import Flask, render_template, request, jsonify
import server.util as util  # ✅ import util inside server folder

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def home():
    return render_template("index.html")  # loads templates/index.html

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    print("🏠 Real Estate Price Prediction app is running...")
    app.run(host="0.0.0.0", port=5000, debug=True)





