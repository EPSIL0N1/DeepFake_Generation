import cv2

sift = cv2.SIFT_create()

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

img1 = cv2.imread("./images/books_image_smallSize.jpg")
img2 = cv2.imread("./images/books_image_smallSize.jpg")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)

# print(len(matches))

img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[2000:5000], img2, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('SIFT', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()