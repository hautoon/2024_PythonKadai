import cv2
import dlib
import numpy as np
from PIL import Image


class FaceGlassesOverlay:
    def __init__(self, predictor_path='shape_predictor_68_face_landmarks.dat'):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(predictor_path)

    def load_image(self, path):
        return cv2.imread(path)

    def resize_image(self, image, width):
        aspect_ratio = float(image.shape[1]) / float(image.shape[0])
        height = int(width / aspect_ratio)
        return cv2.resize(image, (width, height))

    def detect_faces(self, image):
        return self.detector(image, 1)

    def find_face_landmarks(self, image, faces):
        return [self.predictor(image, face) for face in faces]

    def overlay_image(self, l_img, s_img, position, alpha_mask):
        x_offset, y_offset = position
        y1, y2 = y_offset, y_offset + s_img.shape[0]
        x1, x2 = x_offset, x_offset + s_img.shape[1]

        alpha_s = alpha_mask / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                                      alpha_l * l_img[y1:y2, x1:x2, c])

    def apply_glasses_to_faces(self, image_path, glasses_path):
        image = self.load_image(image_path)
        glasses_image = Image.open(glasses_path).convert("RGBA")

        faces = self.detect_faces(image)
        landmarks = self.find_face_landmarks(image, faces)

        for landmark in landmarks:
            left_eye = landmark.part(36)
            right_eye = landmark.part(45)

            glasses_width = right_eye.x - left_eye.x
            scaled_glasses = glasses_image.resize(
                (glasses_width, int(glasses_image.height * glasses_width / glasses_image.width)))
            glasses_np = np.array(scaled_glasses)

            x = left_eye.x
            y = left_eye.y - int(scaled_glasses.height / 5)
            self.overlay_image(image, glasses_np[:, :, :3], (x, y), glasses_np[:, :, 3])

        return image