from flask import Flask, render_template, Response, request
import cv2
import threading
from util import get_limits, yellow, red, green, blue, purple, orange, gray

app = Flask(__name__)

color_to_detect = red  # Default color

cap = cv2.VideoCapture(0)
frame_lock = threading.Lock()

def generate_frames(color):
    global cap
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        with frame_lock:
            hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lowerLimit, upperLimit = get_limits(color=color)
            mask = cv2.inRange(hsv_image, lowerLimit, upperLimit)
            print(f"Hue: {lowerLimit[0]}-{upperLimit[0]}, Saturation: {lowerLimit[1]}-{upperLimit[1]}, Value: {lowerLimit[2]}-{upperLimit[2]}")

            ret, thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY_INV)
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                if cv2.contourArea(cnt) > 200:
                    x1, y1, w, h = cv2.boundingRect(cnt)
                    frame = cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    global color_to_detect
    color_name = request.args.get('color', 'red')  # Default to red if no color is specified
    color_to_detect = color_name.lower()
    
    # Convert color name to BGR value
    if color_to_detect == 'red':
        color_to_detect = red
    elif color_to_detect == 'green':
        color_to_detect = green
    elif color_to_detect == 'yellow':
        color_to_detect = yellow
    elif color_to_detect == 'blue':
        color_to_detect = blue
    elif color_to_detect == 'purple':
        color_to_detect = purple
    elif color_to_detect == 'orange':
        color_to_detect = orange
    elif color_to_detect == 'gray':
        color_to_detect = gray
    else:
        color_to_detect = red  # Default to red if the color is not recognized

    return Response(generate_frames(color=color_to_detect), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
