import os
from typing import List, Dict, Any

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKFLOW_DIR = os.path.join(ROOT_DIR, "workflow")

file_types = [
    ("Image", ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp")),
    ("Video", ("*.mp4", "*.mkv")),
]

source_target_map: List[Dict[str, Any]] = []
simple_map: Dict[str, Any] = {}

source_path: str | None = None
target_path: str | None = None
output_path: str | None = None

frame_processors: List[str] = []
keep_fps: bool = True
keep_audio: bool = True
keep_frames: bool = False
many_faces: bool = False
map_faces: bool = False
poisson_blend: bool = False
color_correction: bool = False
nsfw_filter: bool = False

video_encoder: str | None = None
video_quality: int | None = None

live_mirror: bool = False
live_resizable: bool = True
camera_input_combobox: Any | None = None
webcam_preview_running: bool = False
show_fps: bool = False

max_memory: int | None = None
execution_providers: List[str] = []
execution_threads: int | None = None
headless: bool | None = None
log_level: str = "error"

fp_ui: Dict[str, bool] = {"face_enhancer": False, "face_enhancer_gpen256": False, "face_enhancer_gpen512": False}

face_swapper_enabled: bool = True
opacity: float = 1.0
sharpness: float = 0.0

mouth_mask: bool = False
show_mouth_mask_box: bool = False
mask_feather_ratio: int = 12
mask_down_size: float = 0.1
mask_size: float = 1.0
mouth_mask_size: float = 0.0

enable_interpolation: bool = True
interpolation_weight: float = 0

import threading
dml_lock = threading.Lock()
