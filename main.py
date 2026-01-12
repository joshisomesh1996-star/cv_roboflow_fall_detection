import cv2
from config.settings import DEFAULT_INPUT_VIDEO, DEFAULT_OUTPUT_VIDEO
from inference.roboflow_client import infer_frame
from processing.predictions import normalize_predictions
from processing.visualization import draw_detections
from video.video_io import open_video, create_writer


def main(input_video=DEFAULT_INPUT_VIDEO, output_video=DEFAULT_OUTPUT_VIDEO):
    cap = open_video(input_video)
    writer = create_writer(cap, output_video)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        preds = infer_frame(frame)
        print(preds)
        if preds is None:
            print("Inference failed for frame.")
        detections = normalize_predictions(preds)
        frame = draw_detections(frame, detections)

        writer.write(frame)

        cv2.imshow("Fall Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
