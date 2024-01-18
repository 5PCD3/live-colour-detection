# Live Colour Detection

Live Colour Detection is a computer vision project that enables real-time color detection through a web interface. This project uses OpenCV for image processing, Flask for serving the web application, and allows users to select a color and observe live video feed with real-time color detection.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Live Video Feed:** Displays a live video feed from the camera.
- **Color Detection:** Detects and outlines objects of a selected color in real-time.
- **Color Selection:** Users can choose from various colors such as yellow, red, blue, purple, orange, gray, and green.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/5PCD3/live-colour-detection.git
    cd live-colour-detection
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the `main.py` script:**

    ```bash
    python main.py
    ```

2. **Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/).**

3. **Click on the color buttons to select the color you want to detect.**

4. **Observe the live video feed with real-time color detection.**

## Project Structure

- **main.py:** Flask application for serving the web interface and handling color detection.
- **util.py:** Utility functions for color detection.
- **templates/index.html:** HTML template for the web interface.
- **static/style.css:** CSS styles for styling the web interface.
- **requirements.txt:** List of Python dependencies.

## Dependencies

- **OpenCV (4.6.0.66):** Computer vision library for image processing.
- **NumPy (1.23.4):** Library for numerical operations.
- **Pillow (9.2.0):** Python Imaging Library for image processing.
- **Flask (1.1.4):** Web framework for serving the application.
- **Werkzeug (1.0.1):** WSGI utility library for Flask.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
