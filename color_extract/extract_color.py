import cv2
import numpy as np
import json


def extract_colors(img):
    '''
    applies thresholding and contour detection on image to identify specific regions, and then extracts the dominant color of each region. 
    '''

    image = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    extracted_colors = {}

    if len(contours) >= 10:
        sorted_contours = sorted(
            contours, key=cv2.contourArea, reverse=True)[:10]
        sorted_contours = sorted(
            sorted_contours, key=lambda c: cv2.boundingRect(c)[0])

        for i, contour in enumerate(sorted_contours):
            x, y, w, h = cv2.boundingRect(contour)
            color_roi = image[y:y + h, x:x + w]
            pixel_color = color_roi[0, 0]

            color_name = ['URO', 'BIL', 'KET', 'BLD',
                          'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH'][i]
            rgb_values = [int(pixel_color[2]), int(
                pixel_color[1]), int(pixel_color[0])]

            extracted_colors[color_name] = rgb_values

    return extracted_colors


