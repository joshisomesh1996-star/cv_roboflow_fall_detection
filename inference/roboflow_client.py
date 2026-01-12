import cv2
import requests
from config.settings import INFERENCE_URL


def infer_frame(frame):
    success, img_encoded = cv2.imencode(".jpg", frame)
    if not success:
        return None

    response = requests.post(
        INFERENCE_URL,
        files={"file": img_encoded.tobytes()}
    )

    if response.status_code == 200:
        return response.json()

    print(response.text)
    return None
