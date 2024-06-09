from PIL import Image, ImageEnhance

# Fungsi untuk menyesuaikan luminans, kontras, dan kecerahan
def sesuaikan_gambar(path, luminans, kontras, kecerahan):
    # Muat gambar
    gambar = Image.open(path)

    # Sesuaikan luminans
    enhancer = ImageEnhance.Brightness(gambar)
    gambar = enhancer.enhance(luminans)

    # Sesuaikan kontras
    enhancer = ImageEnhance.Contrast(gambar)
    gambar = enhancer.enhance(kontras)

    # Sesuaikan kecerahan
    enhancer = ImageEnhance.Brightness(gambar)
    gambar = enhancer.enhance(kecerahan)

    # Tampilkan gambar yang telah disesuaikan
    gambar.show()

    # Simpan gambar yang telah disesuaikan
    gambar.save('gambar_sesuaikan.jpg')

# Contoh penggunaan fungsi
sesuaikan_gambar('path/ke/gambar.jpg', 1.2, 1.5, 1.3)
