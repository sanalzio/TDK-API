# Benim TDK API'ım
Benim yazdığım basit bir [TDK](https://sozluk.gov.tr/) api.

![logo](image.svg)

# Kurulumu
Sadece tdk.py dosyasını indirin ve ana kodunuzun bulunduğu klasöre atın.

# Kullanımı
## içeri aktarma
```python3
from tdk import * #tdk modülünü içeri aktarırız
```
## arama yapma
```python3
sonuc = ara("Osmanlı Tokadı")
```
## anlam alma
kod:
```python3
print(sonuc.anlam)
```
çıktı:
> Sert ve etkili tokat
## tüm anlamları alma
kod:
```python3
print(sonuc.anlamlar)
```
çıktı:
> ('Sert ve etkili tokat', 'Sert ve etkili uyarı', 'Ezici üstünlük')
## örnekleri alma
kod:
```python3
print(sonuc.örnekler)
```
çıktı:
> ("Yaradan'a sığınıp Osmanlı tokadını çarptık mı adamı lobut yemişe çeviren biz değil miydik?",)
## çıktının tamamını alma
kod:
```python3
print(sonuc.json)
```
çıktı:
```json
[{'madde_id': '76616', 'kac': '0', 'kelime_no': '86120', 'cesit': '0', 'anlam_gor': '0', 'on_taki': None, 'on_taki_html': None, 'madde': 'Osmanlı tokadı', 'madde_html': '<strong>Osmanlı tokadı</strong>', 'cesit_say': '2', 'anlam_say': '3', 'taki': None, 'cogul_mu': '0', 'ozel_mi': '0', 'egik_mi': '0', 'lisan_kodu': '0', 'lisan': '', 'telaffuz_html': None, 'lisan_html': None, 'telaffuz': None, 'birlesikler': None, 'font': None, 'madde_duz': 'Osmanli tokadi', 'gosterim_tarihi': None, 'anlamlarListe': [{'anlam_id': '102038', 'madde_id': '76616', 'anlam_sira': '1', 'fiil': '0', 'tipkes': '0', 'anlam': 'Sert ve etkili tokat', 'anlam_html': None, 'gos': '0', 'gos_kelime': '0', 'gos_kultur': '0', 'orneklerListe': [{'ornek_id': '32692', 'anlam_id': '102038', 'ornek_sira': '1', 'ornek': "Yaradan'a sığınıp Osmanlı tokadını çarptık 
mı adamı lobut yemişe çeviren biz değil miydik?", 'kac': '1', 'yazar_id': '34', 'yazar_vd': '', 'yazar': [{'yazar_id': 
'34', 'tam_adi': 'Attilâ İlhan', 'kisa_adi': 'A. İlhan', 'ekno': '165'}]}], 'ozelliklerListe': [{'ozellik_id': '19', 'tur': '3', 'tam_adi': 'isim', 'kisa_adi': 'a.', 'ekno': '30'}]}, {'anlam_id': '102039', 'madde_id': '76616', 'anlam_sira 'gos_kultur': '0', 'ozelliklerListe': [{'ozellik_id': '32', 'tur': '4', 'tam_adi': 'mecaz', 'kisa_adi': 'mec.', 'ekno'stünlük', 'anlam_html': None, 'gos': '0', 'gos_kelime': '0', 'gos_kultur': '0', 'ozelliklerListe': [{'ozellik_id': '32'anlı tokadı atmak', 'on_taki': None}, {'madde_id': '76618', 'madde': 'Osmanlı tokadı yemek', 'on_taki': None}]}] ```
