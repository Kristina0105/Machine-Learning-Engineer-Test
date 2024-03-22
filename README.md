# Machine-Learning-Engineer-Test
Machine Learning Engineer Test: Computer Vision

# PDF Wall Detection
walls.py
This script processes a PDF file containing images, detects walls in each image, and outputs the results in a formatted manner.

## Installation

1. Clone the repository or download the script file from mybranch.
2. Install the required dependencies:
```bash
pip install opencv-python numpy PyMuPDF io PIL 

## Usage
1. Ensure you have a PDF file containing images of walls.
2. Replace "example.pdf" in the script with the path to your PDF file.
3. Run the script

## Description
The script first extracts images from each page of the PDF file using fitz. Then, it applies wall detection using OpenCV. Detected walls are formatted into JSON results.

## Functionality
process_pdf(pdf_path): Processes the PDF file and detects walls in each image.
detect_walls(image): Detects walls in a single image using OpenCV.
format_results(detected_walls): Formats the detected walls into a JSON structure.


# PDF Table Extraction
tables.py
This script extracts tables from a PDF file and saves them to a JSON file for further processing.

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies:
```bash  
pip install camelot-py json

## Usage

Ensure you have a PDF file containing tables.
Replace "example.pdf" in the script with the path to your PDF file.
Specify the name of the output JSON file (output_file variable) if needed.
Run the script

## Description
The script utilizes Camelot, a Python library, to extract tables from PDF files. It then formats the tables into JSON and saves them to a file.

## Functionality
extract_tables_from_pdf(pdf_path): Extracts tables from the specified PDF file.
save_tables_to_json(tables_data, output_file): Saves the extracted tables data to a JSON file.

# Flask Inference API
main.py
This Flask API provides an endpoint for performing various types of inference tasks on images.

## Installation

1. Clone the repository or download the script file.
2. Install the required dependencies:

```bash
pip install Flask

## Usage
Run the script:
Send a POST request to the /inference endpoint with the following parameters:
image: Image file to perform inference on.
type: Type of inference to perform (walls, rooms, page_info, tables).
Example request using curl:

curl -X POST -F "image=@path_to_image.jpg" http://localhost:5000/inference?type=walls

## Description
The API receives an image file and a specified type of inference request, then performs inference accordingly. The supported inference types are:

walls: Detects walls in the image.
rooms: Identifies rooms in the image.
page_info: Provides information about the dimensions of the image page.
tables: Extracts tables from the image.

##  API Endpoints
/inference: POST request endpoint for performing inference tasks.
Functionality
perform_inference(image, inference_type): Mock function to perform inference based on the specified type.
/inference: API route to handle inference requests, accepting image files and inference type parameters.
