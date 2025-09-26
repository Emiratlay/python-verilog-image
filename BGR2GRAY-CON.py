import cv2

# fotoğraf import ettim
img = cv2.imread("input.png")

# Siyah-Beyaz Dönüşüm OPENCV BGR normali
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sonucu göster
cv2.imshow("Siyah Beyaz", gray)

# Dosya olarak kaydetmek için
cv2.imwrite("ornek_siyahbeyaz.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
