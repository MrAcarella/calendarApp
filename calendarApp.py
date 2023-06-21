import datetime

kullanicilar = {}
olaylar = {}

def kullanici_kayit():
    ad = input('Ad: ')
    soyad = input('Soyad: ')
    kullanici_adi = input('Kullanýcý Adý: ')
    sifre = input('Þifre: ')
    tc_kimlik = input('TC Kimlik No: ')
    telefon = input('Telefon: ')
    email = input('E-mail: ')
    adres = input('Adres: ')
    kullanici_tipi = input('Kullanýcý Tipi (Admin/Kullanýcý): ')

    kullanici = {
        'ad': ad,
        'soyad': soyad,
        'sifre': sifre,
        'tc_kimlik': tc_kimlik,
        'telefon': telefon,
        'email': email,
        'adres': adres,
        'kullanici_tipi': kullanici_tipi
    }

    kullanicilar[kullanici_adi] = kullanici

    print('Kullanýcý kaydý baþarýyla oluþturuldu.')



def takvimi_goruntule():
    kullanici_adi = input('Kullanýcý Adý: ')
    sifre = input('Þifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullanýcý adý veya þifre hatalý.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktadýr.')
        return

    olay_listesi = olaylar[tarih].get(kullanici_adi, [])

    if len(olay_listesi) > 0:
        print('Olaylar:')
        for olay in olay_listesi:
            print(f'ID: {olay["id"]}')
            print(f'Baþlangýç Zamaný: {olay["baslangic_zamani"]}')
            print(f'Tip: {olay["tip"]}')
            print(f'Açýklama: {olay["aciklama"]}')
            print('---')

        hatirlat = input('Olayý hatýrlatmak ister misiniz? (E/H): ')
        if hatirlat.upper() == 'E':
            hatirlatma_zamani = input('Hatýrlatma Zamaný (GG.AA.YYYY HH:MM): ')
            hatirlatma_tarih, hatirlatma_saat = hatirlatma_zamani.split(" ")
            hatirlatma_tarih = datetime.datetime.strptime(hatirlatma_tarih, '%d.%m.%Y')
            hatirlatma_saat = datetime.datetime.strptime(hatirlatma_saat, '%H:%M')

            simdi = datetime.datetime.now()

            if hatirlatma_tarih.date() < simdi.date() or (hatirlatma_tarih.date() == simdi.date() and hatirlatma_saat.time() < simdi.time()):
                print('Geçersiz hatýrlatma zamaný. Geçmiþ bir zaman veya þu anki zamandan önce bir zaman belirtmelisiniz.')
            else:
                hatirlatma_zamani = datetime.datetime.combine(hatirlatma_tarih.date(), hatirlatma_saat.time())
                zaman_farki = hatirlatma_zamani - simdi
                dakika_farki = zaman_farki.total_seconds() / 60
                print(f'Olay hatýrlatmasý {dakika_farki} dakika sonra yapýlacak.') 

def olay_tanimla():
    kullanici_adi = input('Kullanýcý Adý: ')
    sifre = input('Þifre: ')
    baslangic_zamani = input('Baþlangýç Zamaný (GG.AA.YYYY SS:DD): ')
    tip = input('Olay Tipi: ')
    aciklama = input('Açýklama: ')

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullanýcý adý veya þifre hatalý.')
        return

    tarih, saat = baslangic_zamani.split(" ")

    olay = {
        'id': len(olaylar) + 1,
        'baslangic_zamani': baslangic_zamani,
        'tip': tip,
        'aciklama': aciklama
    }

    if tarih not in olaylar:
        olaylar[tarih] = {}

    if kullanici_adi not in olaylar[tarih]:
        olaylar[tarih][kullanici_adi] = []

    olaylar[tarih][kullanici_adi].append(olay)

    print('Olay baþarýyla tanýmlandý.')

def olay_sil():
    kullanici_adi = input('Kullanýcý Adý: ')
    sifre = input('Þifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')
    olay_id = int(input('Silinecek Olay ID\'si: '))

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullanýcý adý veya þifre hatalý.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktadýr.')
        return

    if kullanici_adi not in olaylar[tarih]:
        print('Belirtilen tarihte kullanýcýya ait olay bulunmamaktadýr.')
        return

    olay_listesi = olaylar[tarih][kullanici_adi]
    olay_bulundu = False

    for olay in olay_listesi:
        if olay['id'] == olay_id:
            olay_listesi.remove(olay)
            olay_bulundu = True
            print('Olay baþarýyla silindi.')
            break

    if not olay_bulundu:
        print('Belirtilen ID\'ye sahip bir olay bulunamadý.')

def olay_guncelle():
    kullanici_adi = input('Kullanýcý Adý: ')
    sifre = input('Þifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')
    olay_id = int(input('Güncellenecek Olay ID\'si: '))

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullanýcý adý veya þifre hatalý.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktadýr.')
        return

    if kullanici_adi not in olaylar[tarih]:
        print('Belirtilen tarihte kullanýcýya ait olay bulunmamaktadýr.')
        return

    olay_listesi = olaylar[tarih][kullanici_adi]
    olay_bulundu = False

    for olay in olay_listesi:
        if olay['id'] == olay_id:
            yeni_baslangic_zamani = input('Yeni Baþlangýç Zamaný (GG.AA.YYYY SS:DD): ')
            yeni_tip = input('Yeni Olay Tipi: ')
            yeni_aciklama = input('Yeni Açýklama: ')

            olay['baslangic_zamani'] = yeni_baslangic_zamani
            olay['tip'] = yeni_tip
            olay['aciklama'] = yeni_aciklama

            print('Olay baþarýyla güncellendi.')
            olay_bulundu = True
            break

    if not olay_bulundu:
        print('Belirtilen ID\'ye sahip bir olay bulunamadý.')

while True:
    print('1- Kullanýcý Kaydý Oluþtur')
    print('2- Takvimi Görüntüle')
    print('3- Olay Tanýmla')
    print('4- Olay Sil')
    print('5- Olay Güncelle')
    print('6- Çýkýþ')

    secim = input('Bir iþlem seçin (1-6): ')

    if secim == '1':
        kullanici_kayit()
    elif secim == '2':
        takvimi_goruntule()
    elif secim == '3':
        olay_tanimla()
    elif secim == '4':
        olay_sil()
    elif secim == '5':
        olay_guncelle()
    elif secim == '6':
        break
    else:
        print('Geçersiz bir seçim yaptýnýz. Lütfen tekrar deneyin.')

