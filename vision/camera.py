"""
==========================================================
Project ULTRON
Vision System
camera.py
==========================================================
"""

import cv2
import threading
import time


class VisionSystem:

    ############################################################

    def __init__(self, config):

        self.config = config

        self.camera = None

        self.running = False

        self.frame = None

        self.thread = None

    ############################################################

    def initialize(self):

        print("[Vision] Starting Camera...")

        self.camera = cv2.VideoCapture(
            self.config.CAMERA_INDEX
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            self.config.FRAME_WIDTH
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            self.config.FRAME_HEIGHT
        )

        if not self.camera.isOpened():

            raise RuntimeError(
                "Unable to open webcam."
            )

        self.running = True

        self.thread = threading.Thread(
            target=self._camera_loop,
            daemon=True
        )

        self.thread.start()

        print("[Vision] Camera Ready")

    ############################################################

    def _camera_loop(self):

        while self.running:

            success, frame = self.camera.read()

            if success:

                self.frame = frame

            time.sleep(0.01)

    ############################################################

    def get_frame(self):

        return self.frame

    ############################################################

    def get_rgb_frame(self):

        if self.frame is None:

            return None

        return cv2.cvtColor(
            self.frame,
            cv2.COLOR_BGR2RGB
        )

    ############################################################

    def show_preview(self):

        while self.running:

            if self.frame is not None:

                cv2.imshow(
                    "ULTRON Camera",
                    self.frame
                )

            key = cv2.waitKey(1)

            if key == ord("q"):

                break

        cv2.destroyAllWindows()

    ############################################################

    def save_image(self, filename):

        if self.frame is None:

            return False

        cv2.imwrite(
            filename,
            self.frame
        )

        print(
            f"[Vision] Image Saved : {filename}"
        )

        return True

    ############################################################

    def shutdown(self):

        self.running = False

        if self.thread is not None:

            self.thread.join(timeout=1)

        if self.camera is not None:

            self.camera.release()

        cv2.destroyAllWindows()

        print("[Vision] Shutdown Complete")
