import cv2


class CannySettings:
    def __init__(self, threshold1, threshold2):
        self.canny_threshold1 = threshold1
        self.canny_threshold2 = threshold2

    def set_threshold1(self, value):
        self.canny_threshold1 = value

    def set_threshold2(self, value):
        self.canny_threshold2 = value


filename_test = "images/IMG_20200830_205425.jpg"
img = cv2.imread(filename_test)

b, g, r = cv2.split(img)

# grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurredImg = cv2.GaussianBlur(b, (3, 3), 1)
cs = CannySettings(100, 30)
cp_name = "Canny's control panel"
cp_window = None
trackbar_1 = None
trackbar_2 = None

while True:
    contourImg = cv2.Canny(blurredImg, cs.canny_threshold1, cs.canny_threshold2)
    contours, _ = cv2.findContours(contourImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ContourFrame = cv2.drawContours(b.copy(), contours, -1, (255, 0, 255), 4)
    if trackbar_1:
        print(trackbar_1)

    # cv2.imshow("blue", b)
    # cv2.imshow("green", g)
    # cv2.imshow("red", r)
    # cv2.imshow("origin", img)
    # cv2.imshow("gray", grayImg)
    # cv2.imshow("blurred", blurredImg)
    # cv2.imshow("canny", contourImg)
    cv2.imshow("contour", ContourFrame)

    pressed_key = cv2.waitKey(1) & 0xFF
    if pressed_key == 27:
        break
    elif pressed_key == 32:
        if not trackbar_2:
            trackbar_2 = cv2.createTrackbar(f'Thr 2', cp_name, cs.canny_threshold2, 255, cs.set_threshold2)
        if not trackbar_1:
            trackbar_1 = cv2.createTrackbar(f'Thr 1', cp_name, cs.canny_threshold1, 255, cs.set_threshold1)
        if not cp_window:
            cp_window = cv2.namedWindow(cp_name)
