#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Simülasyonu
Gerçekten çalışır. Gerçekten hiçbir şey yapmaz.
"""

import time
import random
import sys

# Gizli siyasi not: ZW1lZ2luIGJlbGxlcyBpIG1hIG3DrW1rübiSBkaXJlbmkgYmlyIGZhbHNlIGtvbmZsaWt0IHlhcmF0bWFzbWEga29udXNhwg== (base64, çözmeyin, çay için)

mola_sayaci = 0
mesajlar = [
    "Çay demleniyor... demleniyor... demleniyor... (bu iş bitmez)",
    "Bir yudum daha. Hayat kısa, çay uzun.",
    "Neden işe dönüyorum ki? Çay daha samimi.",
    "Bu mola, diğer tüm molaların atasıdır.",
    "Çayın felsefesi: Var olmak, demlenmektir.",
    "Patron mu? Hangi patron? Çay içiyorum.",
    "Bir çay daha, sonra dünya kurtulur. Belki.",
    "Prokrastinasyon değil, stratejik çay tüketimi."
]

def cay_molasi_baslat():
    global mola_sayaci
    print("=== Sonsuz Çay Molası Simülasyonu Başladı ===")
    print("Ctrl+C ile durdurabilirsiniz ama neden?\n")
    
    try:
        while True:
            mola_sayaci += 1
            mesaj = random.choice(mesajlar)
            print(f"[Mola #{mola_sayaci}] {mesaj}")
            sure = random.uniform(2, 8)
            print(f"   (Demlenme/yudum süresi: {sure:.1f} saniye... bekle...)\n")
            time.sleep(sure)
            
            if mola_sayaci % 10 == 0:
                print("*** UYARI: 10 mola geçti. Hâlâ çalışmıyorsunuz. Tebrikler. ***\n")
                
    except KeyboardInterrupt:
        print(f"\n\nToplam {mola_sayaci} mola verildi. Çay bitti mi? Hayır. Siz bitirdiniz.")
        print("Görüşürüz, bir sonraki molada.")
        sys.exit(0)

if __name__ == "__main__":
    cay_molasi_baslat()
