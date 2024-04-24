from april24_001 import FaceGlassesOverlay
import cv2

def main():
    face_glasses_overlay = FaceGlassesOverlay()
    output_image = face_glasses_overlay.apply_glasses_to_faces('057018e8a3b40e0529b63d2f185fd9ab_t.jpeg', 'megane.png')
    cv2.imshow('Result', output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()