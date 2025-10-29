import cv2
from deepface import DeepFace
import random

emotion_quotes = {
    "happy": [
        "Keep smiling, it makes you beautiful!",
        "Happiness looks gorgeous on you",
        "Stay positive and spread joy everywhere!"
    ],
    "sad": [
        "It's okay to feel sad sometimes, better days are coming",
        "Every storm runs out of rain, don’t give up",
        "You are stronger than you think"
    ],
    "angry": [
        "Take a deep breath — peace begins with you",
        "Don’t let anger control you, let calm guide you",
        "Relax... you got this!"
    ],
    "surprise": [
        "Life is full of surprises! Enjoy the moment",
        "Wow! Something unexpected can be beautiful",
    ],
    "fear": [
        "Courage doesn’t mean you don’t feel fear — it means you act despite it",
        "You are brave, even if you don’t feel like it right now"
    ],
    "neutral": [
        "Every day is a new chance to shine",
        "Stay calm and keep going",
        "Breathe. Relax. You’re doing great!"
    ]
}

def detect_emotion():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return "Camera not detected."

    dominant_emotion = "neutral"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        if isinstance(result, list):
            dominant_emotion = result[0]['dominant_emotion']
        else:
            dominant_emotion = result['dominant_emotion']

        print(f"Detected emotion: {dominant_emotion}")

        cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return random.choice(emotion_quotes.get(dominant_emotion, ["Be yourself — that’s your power"]))
