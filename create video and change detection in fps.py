import cv2
import numpy as np

def video_olustur(uzunluk_saniye=10, fps=30):
    # Video ayarları
    width, height = 640, 480
    video_path = 'olusturulan_video.mp4'

    # VideoWriter objesini oluştur
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

    for saniye in range(uzunluk_saniye * fps):
        # Beyaz ekran oluştur
        frame = np.ones((height, width, 3), np.uint8) * 255

        # 4. saniyede siyah dikdörtgen ekleyin
        if 4 * fps <= saniye < 6 * fps:
            dikdortgen_baslangic = (width // 4, height // 4)
            dikdortgen_bitis = (3 * width // 4, 3 * height // 4)
            frame = cv2.rectangle(frame, dikdortgen_baslangic, dikdortgen_bitis, (0, 0, 0), -1)

        # Frame'i video dosyasına yaz
        out.write(frame)

    # Video dosyasını kapat
    out.release()

    print(f"Oluşturulan video: {video_path}")

# Video oluştur
video_olustur()
