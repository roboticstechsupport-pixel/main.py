"""
==========================================================
Project ULTRON
vision/gesture.py
Hand Gesture Recognition
==========================================================
"""

import cv2
import mediapipe as mp


class GestureRecognizer:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.6
        )

    ####################################################

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        gesture = "Unknown"

        if not results.multi_hand_landmarks:
            return frame, "No Hand"

        for hand in results.multi_hand_landmarks:

            self.mp_draw.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            gesture = self._classify(hand)

        return frame, gesture

    ####################################################

    def _classify(self, hand):

        lm = hand.landmark

        # Finger states
        thumb = lm[4].x < lm[3].x
        index = lm[8].y < lm[6].y
        middle = lm[12].y < lm[10].y
        ring = lm[16].y < lm[14].y
        pinky = lm[20].y < lm[18].y

        fingers = [thumb, index, middle, ring, pinky]

        total = sum(fingers)

        # Open hand
        if total == 5:
            return "Open Palm"

        # Closed fist
        if total == 0:
            return "Fist"

        # Pointing
        if index and not middle and not ring and not pinky:
            return "Pointing"

        # Peace sign
        if index and middle and not ring and not pinky:
            return "Victory"

        # Thumbs up (simple heuristic)
        if thumb and not index and not middle and not ring and not pinky:
            return "Thumbs Up"

        return "Unknown"

    ####################################################

    def release(self):

        self.hands.close()


############################################################

if __name__ == "__main__":

    camera = cv2.VideoCapture(0)

    detector = GestureRecognizer()

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        frame, gesture = detector.detect(frame)

        cv2.putText(
            frame,
            gesture,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

        cv2.imshow("ULTRON Gesture Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    detector.release()

    camera.release()

    cv2.destroyAllWindows()
