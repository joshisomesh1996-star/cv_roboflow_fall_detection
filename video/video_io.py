import cv2


def open_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError(path)
    return cap


def create_writer(cap, output_path):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return cv2.VideoWriter(output_path, fourcc, fps, (w, h))
