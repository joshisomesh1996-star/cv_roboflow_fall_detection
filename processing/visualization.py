import cv2


def draw_detections(frame, detections):
    for d in detections:
        x1 = d["x"] - d["w"] // 2
        y1 = d["y"] - d["h"] // 2
        x2 = d["x"] + d["w"] // 2
        y2 = d["y"] + d["h"] // 2

        cv2.rectangle(frame, (x1, y1), (x2, y2), d["color"], 3)

        cv2.putText(
            frame,
            f'{d["label"]} ({d["confidence"]:.2f})',
            (x1, y1 - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            d["color"],
            2
        )

    return frame
