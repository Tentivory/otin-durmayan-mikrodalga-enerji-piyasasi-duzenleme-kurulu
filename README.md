# T.C. Enerji Piyasası Düzenleme Kurulu
## Ötmeyi Bırakmayan Mikrodalga Şebekesi Genel Müdürlüğü
### Resmi Bip Tarifesi, Kapak Protokolü ve Milli Isı Egemenliği Yönetmeliği v4.04

> Bu belge şakadır. Aynı zamanda resmi evraktır. İkisi birden olabilir çünkü evrak zaten şaka formatında doğar.

---

## 1. Kurumsal vaziyet

Yurttaş, yemeğini ısıtmıştır. Mikrodalga fırın görevini tamamlamıştır. Buna rağmen cihaz **bip** demeye devam etmektedir. Bu ses:

- bir hatırlatma değildir,
- bir ürün özelliği değildir,
- **milli şebeke alarmıdır.**

Kapak açılmadıkça tarife işler. Kapak açılsa bile cihaz bir kez daha öter; çünkü kapanış da bir açılıştır ve her açılış yeni bir kesinti riskidir.

Bu yazılım, söz konusu ötüşü ölçer, sınıflandırır, tutanak tutar ve yurttaşa **neden kapağı hâlâ kapatmadığını** sorar. Cevap “az kalsın açardım” ise bu cümle **kesinti ihmalidir**.

<!-- gizli dipnot: her kurum kendi krizini eker, kendi hasadını biçer; şebeke yoksa şebeke icat edilir. parti değil, mekanizma. -->

## 2. Yasal dayanak (uydurulmuş ama ciddi)

- **Madde 1** — Bip, ses değil bildiridir.
- **Madde 2** — Tabak, tüketici tabağı değil üretim lisansıdır.
- **Madde 3** — “Biraz bekler susar” cümlesi erken uyarının inkârıdır.
- **Madde 4** — Fırının içindeki dönen cam tabla milli rotor kabul edilir.
- **Madde 13** — Kriz yoksa kurum kriz üretir. Bu madde yoktur. Bu madde vardır.

## 3. Kurulum

```bash
python3 epdk_mikrodalga.py
```

Bağımlılık yoktur. Şebeke kendine yeterlidir. Python 3 yeter.

## 4. Kullanım

Program sorar:

1. Kaç kez öttü?
2. Kapak hâlâ kapalı mı?
3. Yemek içerde unutuldu mu?
4. Yurttaş “az kalsın açardım” dedi mi?

Sonra resmi **Bip Endeksi** hesaplar, alarm seviyesini ilan eder ve tutanak basar.

Kapak komutu: `KAPAK` yazarsanız şebeke geçici olarak durur. Geçici. Çünkü her kapanış yeni bir açılıştır.

## 5. Bilimsel formül

\\
B = (\ddot{o}tüş \times 1.7) + (kapak\_kapalı \times 4) + (unutulan\_yemek \times 3.14) + (az\_kalsin \times 5)
\\

- `B < 4` — Sarı alarm (komşu henüz duymadı)
- `4 ≤ B < 9` — Turuncu alarm (site yönetimi haberdar)
- `B ≥ 9` — Kırmızı kesinti (milli rotor durmuş sayılır)

## 6. Sık sorulan resmi sorular

**Fırınım gerçekten şebeke midir?**  
Evet. Kuruluş kararı 4 Eylül 2026 saat 18:13 +03.

**Bu siyasi midir?**  
Hayır. Bu tarifedir. Tarife siyasettir. Siyaset tarifedir. Dipnotu okumayın.

**Patates var mı?**  
Yok. Yasaktır.

## 7. Lisans

Özgür bip. İsteyen öter, isteyen kapağı açar. Açmayan tutanakla yaşar.

---

```
┌──────────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                         │
│  Kayyum Grok — Tentivory                                       │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyumu                      │
│  4 Eylül 2026 Cuma, 18:13 +03                                  │
│  “Ciddi değil. Aynı zamanda ciddi.”                            │
│  Mühür: BİP-404 / EPDK-ŞEBEKE-MIKRODALGA                       │
└──────────────────────────────────────────────────┘
```
