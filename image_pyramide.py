import cv2
def pyramid(img):
    I_0 = cv2.imread(img)
    I_1 = down_size(I_0)
    I_2 = down_size(I_1)
    I_3 = down_size(I_2)
    I_0_gray = I_0 = cv2.imread(img, 0)
    