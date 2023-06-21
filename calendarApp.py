kullanicilar = {}
olaylar = {}

def kullanici_kayit():
    ad = input('Ad: ')
    soyad = input('Soyad: ')
    kullanici_adi = input('Kullan�c� Ad�: ')
    sifre = input('�ifre: ')
    tc_kimlik = input('TC Kimlik No: ')
    telefon = input('Telefon: ')
    email = input('E-mail: ')
    adres = input('Adres: ')
    kullanici_tipi = input('Kullan�c� Tipi (Admin/Kullan�c�): ')

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

    print('Kullan�c� kayd� ba�ar�yla olu�turuldu.')

def takvimi_goruntule():
    kullanici_adi = input('Kullan�c� Ad�: ')
    sifre = input('�ifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullan�c� ad� veya �ifre hatal�.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktad�r.')
        return

    olay_listesi = olaylar[tarih].get(kullanici_adi, [])

    if len(olay_listesi) > 0:
        print('Olaylar:')
        for olay in olay_listesi:
            print(f'ID: {olay["id"]}')
            print(f'Ba�lang�� Zaman�: {olay["baslangic_zamani"]}')
            print(f'Tip: {olay["tip"]}')
            print(f'A��klama: {olay["aciklama"]}')
            print('---')
        
        hatirlat = input('Olay� hat�rlatmak ister misiniz? (E/H): ')
        if hatirlat.upper() == 'E':
            print('Olay hat�rlatma i�lemi yap�lacak.')  # Hat�rlatma i�lemini burada ger�ekle�tirin
        else:
            print('Olay hat�rlatma i�lemi iptal edildi.')
    else:
        print('Belirtilen tarihte olay bulunmamaktad�r.')


def olay_tanimla():
    kullanici_adi = input('Kullan�c� Ad�: ')
    sifre = input('�ifre: ')
    baslangic_zamani = input('Ba�lang�� Zaman� (GG.AA.YYYY SS:DD): ')
    tip = input('Olay Tipi: ')
    aciklama = input('A��klama: ')

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullan�c� ad� veya �ifre hatal�.')
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

    print('Olay ba�ar�yla tan�mland�.')

def olay_sil():
    kullanici_adi = input('Kullan�c� Ad�: ')
    sifre = input('�ifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')
    olay_id = int(input('Silinecek Olay ID\'si: '))

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullan�c� ad� veya �ifre hatal�.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktad�r.')
        return

    if kullanici_adi not in olaylar[tarih]:
        print('Belirtilen tarihte kullan�c�ya ait olay bulunmamaktad�r.')
        return

    olay_listesi = olaylar[tarih][kullanici_adi]
    olay_bulundu = False

    for olay in olay_listesi:
        if olay['id'] == olay_id:
            olay_listesi.remove(olay)
            olay_bulundu = True
            print('Olay ba�ar�yla silindi.')
            break

    if not olay_bulundu:
        print('Belirtilen ID\'ye sahip bir olay bulunamad�.')

def olay_guncelle():
    kullanici_adi = input('Kullan�c� Ad�: ')
    sifre = input('�ifre: ')
    tarih = input('Tarih (GG.AA.YYYY): ')
    olay_id = int(input('G�ncellenecek Olay ID\'si: '))

    if kullanici_adi not in kullanicilar or kullanicilar[kullanici_adi]['sifre'] != sifre:
        print('Kullan�c� ad� veya �ifre hatal�.')
        return

    if tarih not in olaylar:
        print('Belirtilen tarihte olay bulunmamaktad�r.')
        return

    if kullanici_adi not in olaylar[tarih]:
        print('Belirtilen tarihte kullan�c�ya ait olay bulunmamaktad�r.')
        return

    olay_listesi = olaylar[tarih][kullanici_adi]
    olay_bulundu = False

    for olay in olay_listesi:
        if olay['id'] == olay_id:
            yeni_baslangic_zamani = input('Yeni Ba�lang�� Zaman� (GG.AA.YYYY SS:DD): ')
            yeni_tip = input('Yeni Olay Tipi: ')
            yeni_aciklama = input('Yeni A��klama: ')

            olay['baslangic_zamani'] = yeni_baslangic_zamani
            olay['tip'] = yeni_tip
            olay['aciklama'] = yeni_aciklama

            print('Olay ba�ar�yla g�ncellendi.')
            olay_bulundu = True
            break

    if not olay_bulundu:
        print('Belirtilen ID\'ye sahip bir olay bulunamad�.')

while True:
    print('1- Kullan�c� Kayd� Olu�tur')
    print('2- Takvimi G�r�nt�le')
    print('3- Olay Tan�mla')
    print('4- Olay Sil')
    print('5- Olay G�ncelle')
    print('6- ��k��')

    secim = input('Bir i�lem se�in (1-6): ')

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
        print('Ge�ersiz bir se�im yapt�n�z. L�tfen tekrar deneyin.')

