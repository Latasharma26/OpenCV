# Learning OpenCV with Python

Welcome to my Learning OpenCV repository! This project serves as a personal collection of Python scripts, exercises, and concepts related to OpenCV, a powerful library for computer vision and image processing.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Topics Covered](#topics-covered)
- [File Descriptions](#file-descriptions)
- [Learning Resources](#learning-resources)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This repository contains code snippets and exercises that I have created and used while learning OpenCV. The focus of this repository is to explore the various functionalities that OpenCV offers, including face detection, image manipulation, color spaces, and more.

## Installation
To get started with the scripts, you'll need Python 3.x installed along with OpenCV and NumPy libraries. Install the necessary dependencies by running:

```bash
pip install opencv-python numpy
```

Ensure your environment is set up to support image and video file handling.

## Topics Covered
This repository covers the following OpenCV concepts and functionalities:

- Basic Image Manipulation (resizing, rescaling, transformations)
- Face, Eye, and Smile Detection using Haar Cascades
- Image Filtering (blurring, thresholding)
- Color Spaces (conversions between BGR, RGB, HSV, etc.)
- Bitwise Operations (AND, OR, XOR, NOT)
- Contour Detection (finding shapes, edges)
- Gradients and Edge Detection (Sobel, Laplacian)
- Histogram Equalization (improving image contrast)
- Masking and ROI (Region of Interest)

## File Descriptions
Here’s a list of the scripts and their functionalities:

- **Real_time_Face_Detection.py**: Real-time face detection using webcam and OpenCV.
- **basic.py**: Demonstrates basic image operations like resizing and displaying images.
- **bitwise.py**: Illustrates how to perform bitwise operations on images.
- **blurring.py**: Shows how to apply different types of blurs to an image.
- **colour_spaces.py**: Converts images between different color spaces such as BGR, RGB, and HSV.
- **counters.py**: Detects contours and draws them on images.
- **draw.py**: Demonstrates how to draw basic shapes (like circles, rectangles) on images.
- **eye_detect.py**: Detects eyes in images using Haar Cascades.
- **face_detect.py**: Basic face detection using pre-trained Haar Cascades.
- **gradients.py**: Demonstrates gradient operations (Sobel, Laplacian) for edge detection.
- **haar_face.xml, haarcascade_eye.xml, haarcascade_frontalface_default.xml, haarcascade_smile.xml**: Pre-trained Haar Cascades for face, eye, and smile detection.
- **histogram.py**: Applies histogram equalization for improving image contrast.
- **masking.py**: Masks parts of an image to focus on specific regions.
- **read.py**: Basic script to read, display, and save images using OpenCV.
- **rescale.py**: Resizes images to different scales.
- **smile_detect.py**: Detects smiles in an image using Haar Cascades.
- **splitmerge.py**: Splits an image into its individual channels and merges them back.
- **thresh.py**: Demonstrates thresholding techniques (binary, adaptive, etc.).
- **transformation.py**: Shows how to rotate, translate, and apply affine transformations to images.

## Learning Resources
Here are some helpful resources I used while learning OpenCV:

- [OpenCV Official Documentation](https://docs.opencv.org)
- [OpenCV Python Tutorials](https://www.youtube.com/watch?v=oXlwWbU8l2o&t=10368s&ab_channel=freeCodeCamp.org)
- [OpenCV on GitHub](https://github.com/opencv/opencv)
- [Real Python - OpenCV Guide](https://realpython.com/)

Feel free to explore these resources as you go through the code.

## Contributing
As this repository is part of my personal learning journey, contributions are not expected. However, if you spot any issues or have suggestions, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
