import cv2


class CannySettings:
    def __init__(self, threshold1, threshold2):
        self.canny_threshold1 = threshold1
        self.canny_threshold2 = threshold2

    def set_threshold1(self, value):
        self.canny_threshold1 = value

    def set_threshold2(self, value):
        self.canny_threshold2 = value


def contour_refresh():
    contour_img = cv2.Canny(blurredImg, cs.canny_threshold1, cs.canny_threshold2)
    contours, _ = cv2.findContours(contour_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_frame = cv2.drawContours(b.copy(), contours, -1, (255, 0, 255), 4)
    cv2.imshow(preview_window_name, contour_frame)


def set_and_refresh_threshold1(value):
    cs.set_threshold1(value)
    contour_refresh()


def set_and_refresh_threshold2(value):
    cs.set_threshold2(value)
    contour_refresh()


filename_test = "IMG_20200830_205425.jpg"
# init preview window
preview_window_name = "pyPhotoCrop - Preview Contour"
preview_window = cv2.namedWindow(preview_window_name, cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_NORMAL)

img = cv2.imread(f'images/{filename_test}')

b, g, r = cv2.split(img)
blurredImg = cv2.GaussianBlur(b, (3, 3), 1)
cs = CannySettings(100, 30)
cp_name = "Canny control panel"
cp_window = None
trackbar_1 = None
trackbar_2 = None


contourFrame = None


contour_refresh()

while True:
    pressed_key = cv2.waitKey(0) & 0xFF
    if pressed_key == 27:
        cv2.destroyAllWindows()
    elif pressed_key == 32:
        cp_window = cv2.namedWindow(cp_name)
        trackbar_2 = cv2.createTrackbar(f'Thr 2', cp_name, cs.canny_threshold2, 255, set_and_refresh_threshold2)
        trackbar_1 = cv2.createTrackbar(f'Thr 1', cp_name, cs.canny_threshold1, 255, set_and_refresh_threshold1)
    else:
        pass
