#  Python ile Görüntü İşleme: Fotoğrafı Siyah-Beyaz Yapma

Bu proje, OpenCV kullanarak bir fotoğrafı **siyah-beyaz** (gri tonlama) yapmayı gösterir. 

##  Gereksinimler
Öncelikle OpenCV kütüphanesini yükleyin:

```bash
pip install opencv-python 
````
````Python
import cv2

# Fotoğrafı oku
img = cv2.imread("input.png")

# Siyah-Beyaz (gri tonlama) dönüşüm
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sonucu ekranda göster
cv2.imshow("Siyah Beyaz", gray)

# Dosya olarak kaydet
cv2.imwrite("ornek_siyahbeyaz.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

Girdi: input.png
Çıktı: ornek_siyahbeyaz.jpg
````

