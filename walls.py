import cv2
import numpy as np
import fitz
from PIL import Image
import io

def process_pdf(pdf_path):
    images = []
    doc = fitz.open(pdf_path)
    for page in doc:
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            images.append(image)
    for image in images:
        detect_walls(image)


def detect_walls(image):

    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    if lines is None:
        print("Прямих ліній не виявлено.")
        return

    detected_walls = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        detected_walls.append({"start_x": x1, "start_y": y1, "end_x": x2, "end_y": y2})

    wall_results = format_results(detected_walls)
    print(wall_results)

def format_results(detected_walls):
    wall_results = []
    for index, wall in enumerate(detected_walls):
        result = {
            "wallId": index,
            "position": {
                "start": {"x": wall['start_x'], "y": wall['start_y']},
                "end": {"x": wall['end_x'], "y": wall['end_y']}
            },
            "confidence": 1.0
        }
        wall_results.append(result)
    return {"type": "walls", "detectionResults": {"walls": wall_results}}



if __name__ == "__main__":
    pdf_path = "example.pdf" # Replace 'example.pdf' with the path to your PDF file
    process_pdf(pdf_path)
