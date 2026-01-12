from config.settings import CONF_THRESHOLD


def normalize_predictions(predictions):
    if not predictions or "predictions" not in predictions:
        return []

    detections = []

    for pred in predictions["predictions"]:
        if pred["confidence"] < CONF_THRESHOLD:
            continue

        cls = pred["class"].lower()

        if cls == "fall":
            label = "standing"
            color = (0, 255, 0)
        elif cls == "stand":
            label = "falling"
            color = (0, 0, 255)
        else:
            label = cls
            color = (255, 255, 0)

        detections.append({
            "x": int(pred["x"]),
            "y": int(pred["y"]),
            "w": int(pred["width"]),
            "h": int(pred["height"]),
            "confidence": pred["confidence"],
            "label": label,
            "color": color
        })

    return detections
