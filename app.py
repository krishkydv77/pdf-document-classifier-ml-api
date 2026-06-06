from flask import Flask, request, jsonify
import joblib
app = Flask(__name__)
model = joblib.load("models/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data=request.get_json()
        text_input=data.get("text","")

        if not text_input.strip():
            return jsonify({"error": "Empty text"}), 400
    
        prediction = model.predict([text_input])
        return jsonify({
            "prediction": prediction[0]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)



    """
  postman   {
  "text": "invoice payment gst amount total due"
}
"""