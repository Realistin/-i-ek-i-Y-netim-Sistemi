import os

CIÇEK_DOSYA = "data/cicekler.txt"
SIPARIS_DOSYA = "data/siparisler.txt"

def cicekleri_yukle():
    cicekler = {}
    try:
        with open(CIÇEK_DOSYA, "r", encoding="utf-8") as f:
            for satir in f:
                ad, stok, fiyat = satir.strip().split(",")
                cicekler[ad] = {"stok": int(stok), "fiyat": float(fiyat)}
    except FileNotFoundError:
        pass
    return cicekler

def cicekleri_kaydet(cicekler):
    with open(CIÇEK_DOSYA, "w", encoding="utf-8") as f:
        for ad, veri in cicekler.items():
            f.write(f"{ad},{veri['stok']},{veri['fiyat']}
")

def cicek_ekle(cicekler):
    ad = input("Çiçek adı: ")
    if ad in cicekler:
        print("Bu çiçek zaten var.")
        return
    try:
        stok = int(input("Stok adedi: "))
        fiyat = float(input("Birim fiyatı: "))
        cicekler[ad] = {"stok": stok, "fiyat": fiyat}
        print("Çiçek eklendi.")
    except ValueError:
        print("Geçersiz giriş.")

def cicek_sil(cicekler):
    ad = input("Silinecek çiçek adı: ")
    if ad in cicekler:
        del cicekler[ad]
        print("Çiçek silindi.")
    else:
        print("Çiçek bulunamadı.")

def siparis_al(cicekler):
    ad = input("Müşteri adı: ")
    cicek_adi = input("Sipariş edilen çiçek: ")
    if cicek_adi in cicekler:
        try:
            adet = int(input("Adet: "))
            if adet <= cicekler[cicek_adi]["stok"]:
                cicekler[cicek_adi]["stok"] -= adet
                with open(SIPARIS_DOSYA, "a", encoding="utf-8") as f:
                    f.write(f"{ad},{cicek_adi},{adet}\n")
                print("Sipariş kaydedildi.")
            else:
                print("Yetersiz stok!")
        except ValueError:
            print("Geçersiz adet.")
    else:
        print("Çiçek bulunamadı.")

def stok_kontrol(cicekler):
    for ad, veri in cicekler.items():
        durum = "DÜŞÜK" if veri["stok"] < 5 else "YETERLİ"
        print(f"{ad}: {veri['stok']} adet - {durum}")

def raporla():
    satis = {}
    try:
        with open(SIPARIS_DOSYA, "r", encoding="utf-8") as f:
            for satir in f:
                _, cicek, adet = satir.strip().split(",")
                satis[cicek] = satis.get(cicek, 0) + int(adet)
        print("📝 En çok satılan çiçekler:")
        for ad, adet in sorted(satis.items(), key=lambda x: x[1], reverse=True):
            print(f"{ad}: {adet} adet")
    except FileNotFoundError:
        print("Henüz sipariş yok.")

def menu():
    cicekler = cicekleri_yukle()
    while True:
        print("\n1. Çiçek Ekle\n2. Çiçek Sil\n3. Sipariş Al\n4. Stok Takibi\n5. Raporlama\n6. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            cicek_ekle(cicekler)
        elif secim == "2":
            cicek_sil(cicekler)
        elif secim == "3":
            siparis_al(cicekler)
        elif secim == "4":
            stok_kontrol(cicekler)
        elif secim == "5":
            raporla()
        elif secim == "6":
            cicekleri_kaydet(cicekler)
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    menu()
