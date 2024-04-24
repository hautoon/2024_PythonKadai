import cv2
import matplotlib.pyplot as plt
image = cv2.imread('../057018e8a3b40e0529b63d2f185fd9ab_t.jpeg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap='gray')
plt.show()
cascade = cv2.CascadeClassifier('/Users/hauto/PycharmProjects/pythonProject2/haarcascade_frontalface_default.xml')
boxes = cascade.detectMultiScale(image_gray)
image_output = image.copy()

for x, y, w, h in boxes:
    face = image[y: y + h, x: x + w]
    cv2.rectangle(image_output, (x, y), (x + w, y + h), (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(image_output, cv2.COLOR_BGR2RGB))
plt.show()