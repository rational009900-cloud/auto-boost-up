from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

CARS = [
    {"id": "thar", "name": "Mahindra Thar", "origin": "Indian", "type": "SUV"},
    {"id": "nexon", "name": "Tata Nexon", "origin": "Indian", "type": "SUV"},
    {"id": "swift", "name": "Maruti Suzuki Swift", "origin": "Indian", "type": "Hatchback"},
    {"id": "creta", "name": "Hyundai Creta", "origin": "Indian", "type": "SUV"},
    {"id": "bmw-m4", "name": "BMW M4", "origin": "Foreign", "type": "Coupe"},
    {"id": "mustang", "name": "Ford Mustang", "origin": "Foreign", "type": "Muscle car"},
    {"id": "huracan", "name": "Lamborghini Huracán", "origin": "Foreign", "type": "Supercar"},
    {"id": "911", "name": "Porsche 911", "origin": "Foreign", "type": "Sports car"},
]

@app.get("/")
def home():
    return render_template("index.html", cars=CARS)

@app.post("/api/build")
def save_build():
    data = request.get_json(silent=True) or {}
    allowed = {"car", "paint", "wheel", "spoiler", "bodykit", "underglow", "tint", "ride"}
    build = {key: data.get(key) for key in allowed if key in data}
    return jsonify({"ok": True, "message": "Build configuration received.", "build": build})

if __name__ == "__main__":
    app.run(debug=True)
