import mediapipe as mp
import cv2
import numpy as np

# 画像を表す型エイリアス
Image = np.ndarray
# opencvがアクセスするウェブカメラのID
WEBCAM_ID = 0


def take_photo() -> Image:
    """
    ウェブカメラを使って画像の撮影を行う

    Returns
    -------
    image : np.ndarray
        撮影した画像

    Raises
    ------
    ValueError
        画像の撮影に失敗した
    """
    cap = cv2.VideoCapture(WEBCAM_ID)
    success, image = cap.read()
    if not success:
        raise ValueError("画像の撮影に失敗")
    return image


def face_detection(image: Image) -> bool:
    """
    mediapipeによる顔検出を行う

    Parameters
    ----------
    image : np.ndarray
        解析を行う画像
    
    Returns
    -------
    bool : 顔が検出されたらtrue、されなかったらfalse

    Note
    ----
    複数の顔を認識して個人を識別することが難しいため、
    写真を一人分に分割してその写真から顔が検出できれば出席というふうに判定
    """
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    with mp_face_detection.FaceDetection(
        model_selection=0, min_detection_confidence=0.5
    ) as face_detection:
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            if __debug__:
                # 認識した顔を画像に描画
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
            return True
        if __debug__:
            # 認識した画像を表示
            cv2.imshow("MediaPipe Face Detection", cv2.flip(image, 1))
            cv2.waitKey(0)
        return False


def desk_analysis(image: Image):
    """
    opencvによる机の解析を用いた出席判定解析を行う

    Parameters
    ----------
    image : np.ndarray
        解析を行う画像

    Returns
    -------
    result
        解析した結果
    
    Note
    ----
    - Dead code
    - 使用非推奨
    """
    pass
