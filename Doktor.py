from Personel import Personel
class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def __str__(self):
        return f"{super().__str__()}, Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"

    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def maas_arttir(self):
        yeni_maas = self.get_maas()
        if self.__deneyim_yili >= 15:
            yeni_maas += yeni_maas * 0.20
        elif self.__deneyim_yili >= 10:
            yeni_maas += yeni_maas * 0.15
        elif self.__deneyim_yili >= 5:
            yeni_maas += yeni_maas * 0.10
        self.set_maas(yeni_maas)
