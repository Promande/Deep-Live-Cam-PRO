import os
import cv2
import numpy as np


def imread_unicode(path, flags=cv2.IMREAD_COLOR):
    try:
        data = np.fromfile(path, dtype=np.uint8)
        if data.size == 0:
            return None
        return cv2.imdecode(data, flags)
    except Exception:
        return None


def imwrite_unicode(path, img, params=None):
    try:
        root, ext = os.path.splitext(path)
        if not ext:
            ext = ".png"
        result, encoded_img = cv2.imencode(ext, img, params if params is not None else [])
        if not result:
            return False
        encoded_img.tofile(path)
        return True
    except Exception:
        return False
