import pandas as pd
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
from Personel import Personel

def main():
    try:
        # Personel nesneleri
        personel1 = Personel(1, "Kemal", "Yılmaz", "İdari", 8000)
        personel2 = Personel(2, "Fatma", "Demir", "Depo", 7500)

        print(personel1.__str__())
        print(personel2.__str__())

        # Doktor nesneleri
        doktor1 = Doktor(3, "Ali", "Türk", "Kardiyoloji", 15000, "Kalp Cerrahisi", 10, "ABC Hastanesi")
        doktor2 = Doktor(4, "Ayşe", "Yıldır", "Nöroloji", 16000, "Beyin Cerrahisi", 12, "DEF Hastanesi")
        doktor3 = Doktor(5, "Ahmet Salih", "Kaya", "Ortopedi", 14000, "Kemik Cerrahisi", 4, "GHI Hastanesi")

        doktor1.maas_arttir()
        doktor2.maas_arttir()
        doktor3.maas_arttir()

        print(doktor1.__str__())
        print(doktor2.__str__())
        print(doktor3.__str__())

        # Hemşire nesneleri
        hemsire1 = Hemsire(6, "Zeynep", "Demir", "Acil", 5000, 40, "Temel İlk Yardım", "JKL Hastanesi")
        hemsire2 = Hemsire(7, "Canan", "Öztürk", "Yoğun Bakım", 8500, 35, "Yoğun Bakım Uzmanı", "MNO Hastanesi")
        hemsire3 = Hemsire(8, "Erkan", "Kara", "Pediatri", 4800, 38, "Çocuk Bakımı", "PQR Hastanesi")

        hemsire1.maas_arttir()
        hemsire2.maas_arttir()
        hemsire3.maas_arttir()

        print(hemsire1.__str__())
        print(hemsire2.__str__())
        print(hemsire3.__str__())

        # Hasta nesneleri
        hasta1 = Hasta(1, "Furkan", "Çelik", "1980-01-01", "Kalp Rahatsızlığı", "Cerrahi Müdahale")
        hasta2 = Hasta(2, "Ece", "Kaynak", "1992-05-23", "Soğuk Algınlığı", "İlaç Tedavisi")
        hasta3 = Hasta(3, "Murat", "Koç", "1985-09-15", "Kırık", "Alçı")

        print(hasta1.__str__())
        print(hasta2.__str__())
        print(hasta3.__str__())

        print(f"Tedavi Süresi: {hasta1.tedavi_suresi_hesapla()} gün")
        print(f"Tedavi Süresi: {hasta2.tedavi_suresi_hesapla()} gün")
        print(f"Tedavi Süresi: {hasta3.tedavi_suresi_hesapla()} gün")

        # Pandas DataFrame oluşturma
        data = {
            "personel_no": [personel1.get_personel_no(), personel2.get_personel_no(),
                            doktor1.get_personel_no(), doktor2.get_personel_no(),
                            doktor3.get_personel_no(), hemsire1.get_personel_no(),
                            hemsire2.get_personel_no(), hemsire3.get_personel_no(), None, None, None],
            "ad": [personel1.get_ad(), personel2.get_ad(), doktor1.get_ad(), doktor2.get_ad(), doktor3.get_ad(),
                   hemsire1.get_ad(), hemsire2.get_ad(), hemsire3.get_ad(), hasta1.get_ad(), hasta2.get_ad(), hasta3.get_ad()],
            "soyad": [personel1.get_soyad(), personel2.get_soyad(), doktor1.get_soyad(), doktor2.get_soyad(), doktor3.get_soyad(),
                      hemsire1.get_soyad(), hemsire2.get_soyad(), hemsire3.get_soyad(), hasta1.get_soyad(), hasta2.get_soyad(), hasta3.get_soyad()],
            "departman": [personel1.get_departman(), personel2.get_departman(), doktor1.get_departman(), doktor2.get_departman(),
                          doktor3.get_departman(), hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(), None, None, None],
            "maas": [personel1.get_maas(), personel2.get_maas(), doktor1.get_maas(), doktor2.get_maas(), doktor3.get_maas(),
                     hemsire1.get_maas(), hemsire2.get_maas(), hemsire3.get_maas(), None, None, None],
            "uzmanlik": [None, None, doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(), None, None, None, None, None, None],
            "deneyim_yili": [None, None, doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(), None, None, None, None, None, None],
            "hastane": [None, None, doktor1.get_hastane(), doktor2.get_hastane(), doktor3.get_hastane(), hemsire1.get_hastane(),
                        hemsire2.get_hastane(), hemsire3.get_hastane(), None, None, None],
            "calisma_saati": [None, None, None, None, None, hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(), None, None, None],
            "sertifika": [None, None, None, None, None, hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(), None, None, None],
            "hasta_no": [None, None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta2.get_hasta_no(), hasta3.get_hasta_no()],
            "dogum_tarihi": [None, None, None, None, None, None, None, None, hasta1.get_dogum_tarihi(), hasta2.get_dogum_tarihi(), hasta3.get_dogum_tarihi()],
            "hastalik": [None, None, None, None, None, None, None, None, hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()],
            "tedavi": [None, None, None, None, None, None, None, None, hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()]
        }

        df = pd.DataFrame(data)

        # Boş olan değişken değerleri için 0 atama
        df.fillna(0, inplace=True)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
        doktor_sayisi = df[df['uzmanlik'] != 0].groupby('uzmanlik').size()
        print(f"Doktor sayısı (uzmanlık alanına göre): {sum(doktor_sayisi)}")
        print(doktor_sayisi)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
        bes_yil_doktor = df[(df['deneyim_yili'] > 5) & (df['deneyim_yili'] != 0)].shape[0]
        print(f"5 yıldan fazla deneyime sahip doktorların toplam sayısı: {bes_yil_doktor}")

        # Hasta adına göre DataFrame’i alfabetik olarak sıralama
        df_hastalar = df[df['hasta_no'] != 0]
        df_sorted = df_hastalar.sort_values(by=['ad'])
        print("Hasta adına göre sıralı DataFrame:")
        print(df_sorted)

        # Maaşı 7000 TL üzerinde olan personelleri bulma
        maas_7000_ustu = df[df['maas'] > 7000]
        print("Maaşı 7000 TL üzerinde olan personeller:")
        print(maas_7000_ustu)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
        df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'])
        dogum_1990_sonrasi = df[df['dogum_tarihi'] >= '1990-01-01']
        print("Doğum tarihi 1990 sonrası olan hastalar:")
        print(dogum_1990_sonrasi)


        # Yeni DataFrame oluşturma
        yeni_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
        print("Yeni DataFrame:")
        print(yeni_df)

    except Exception:
        print(f"Bir hata oluştu:")

if __name__ == "__main__":
    main()
