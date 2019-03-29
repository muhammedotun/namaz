import json
import requests
from datetime import datetime
bu_gün = datetime.now()  # bu günün tarihini aldık.
bu_gün = str(bu_gün.day) + '.' + bu_gün.strftime("%m") + '.' + str(bu_gün.year)  # gün.ay.yıl formatına çevirdik.
saat = datetime.now().hour
dakika = datetime.now().minute
json_verisi = open("/home/muhammed/projects/namaz/namaz.json", 'r')
veri = json.load(json_verisi)
vakitler = ["Imsak",
            "Gunes",
            "Ogle",
            "Ikindi",
            "Aksam",
            "Yatsi"]

for item in veri:
    if item['MiladiTarihKisa'] == bu_gün:
        for vakit in vakitler:
            _saat = int(item[vakit].split(':')[0])
            _dakika = int(item[vakit].split(':')[1])
            _yatsı_saat = int(item["Yatsi"].split(':')[0])
            _yatsı_dakika = int(item['Yatsi'].split(':')[1])
            şuanki_saatin_dakika_cinsinden_değeri = saat * 60 + dakika
            vaktin_dakika_cinsinden_değeri = _saat * 60 + _dakika
            v_yatsı = _yatsı_saat*60 + _yatsı_dakika
            if şuanki_saatin_dakika_cinsinden_değeri < vaktin_dakika_cinsinden_değeri:
                if _dakika - dakika < 0:
                    print(vakit, " ezanına ", _saat - saat - 1, " saat ", _dakika - dakika + 60, "dakika var.")
                    Güncel_mi = True
                    break
                else:
                    print(vakit, " ezanına ", _saat - saat, " saat ", _dakika - dakika, "dakika var.")
                    Güncel_mi = True
                    break
            # TODO idareten bir düzeltme yapıldı boş vakitte tekrar düzeltilmesi gerek
            if v_yatsı < şuanki_saatin_dakika_cinsinden_değeri and şuanki_saatin_dakika_cinsinden_değeri < 24*60:
                print("sabaha daha çok var.")
                Güncel_mi = True
                break

def güncelle():
    response = requests.get("https://ezanvakti.herokuapp.com/vakitler?ilce=17911")
    dosya = open("namaz.json", "w")
    dosya.write(response.text)
    dosya.close()
    print("Veri Tabanı Güncellendi. \nTekrar çalıştırın.")
