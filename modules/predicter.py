import importlib.util
import os

import numpy

if "KERAS_BACKEND" not in os.environ:
    for _backend in ("torch", "tensorflow", "jax"):
        if importlib.util.find_spec(_backend) is not None:
            os.environ["KERAS_BACKEND"] = _backend
            break

import opennsfw2
from PIL import Image
import cv2
import modules.globals
from modules.gpu_processing import gpu_cvt_color

from modules.typing import Frame

MAX_PROBABILITY = 0.85

model = None

def predict_frame(target_frame: Frame) -> bool:
    if modules.globals.color_correction:
        target_frame = gpu_cvt_color(target_frame, cv2.COLOR_BGR2RGB)
        
    image = Image.fromarray(target_frame)
    image = opennsfw2.preprocess_image(image, opennsfw2.Preprocessing.YAHOO)
    global model
    if model is None: 
        model = opennsfw2.make_open_nsfw_model()
        
    views = numpy.expand_dims(image, axis=0)
    _, probability = model.predict(views)[0]
    return probability > MAX_PROBABILITY


def predict_image(target_path: str) -> bool:
    return opennsfw2.predict_image(target_path) > MAX_PROBABILITY


def predict_video(target_path: str) -> bool:
    _, probabilities = opennsfw2.predict_video_frames(video_path=target_path, frame_interval=100)
    return any(probability > MAX_PROBABILITY for probability in probabilities)
