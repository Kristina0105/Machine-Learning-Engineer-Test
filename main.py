from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock function to perform inference based on the specified type
def perform_inference(image, inference_type):
    if inference_type == "walls":
        return {"walls": [{"start_x": 100, "start_y": 50, "end_x": 200, "end_y": 250}]}
    elif inference_type == "rooms":
        return {"rooms": ["Living Room", "Bedroom", "Kitchen"]}
    elif inference_type == "page_info":
        return {"page_info": {"width": 800, "height": 600}}
    elif inference_type == "tables":
        return {"tables": [{"tableName": "Table 1", "columns": [{"header": ["A", "B"], "rows": [1, 2]}]}]}
    else:
        return {"error": "Invalid inference type"}

# API endpoint to handle inference requests
@app.route('/inference', methods=['POST'])
def inference():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']

    inference_type = request.args.get('type')
    if not inference_type:
        return jsonify({"error": "Missing 'type' parameter"}), 400

    inference_result = perform_inference(image, inference_type)

    return jsonify(inference_result), 200

if __name__ == '__main__':
    app.run(debug=True)
