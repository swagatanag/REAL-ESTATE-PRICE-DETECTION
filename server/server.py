from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    # Renders your index.html
    return render_template("index.html")

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.form if request.form else request.json

    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Flask server for Real Estate Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)




