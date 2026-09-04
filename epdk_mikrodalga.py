#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. EPDK — Ötmeyi Bırakmayan Mikrodalga Şebekesi.

Gerçekten çalışır. Fırınlar artık şebekedir.
Gizli madde: kriz yoksa kurum kriz üretir. Parti değil, mekanizma.
"""

from __future__ import annotations

import datetime as dt
import random
import sys

MUHUR = "BİP-404 / EPDK-ŞEBEKE-MIKRODALGA"
KAYYUM = "Kayyum Grok — Tentivory"
TARIH = "4 Eylül 2026 Cuma, 18:13 +03"


def evet_mi(s: str) -> bool:
    s = (s or "").strip().lower()
    return s in {"e", "evet", "y", "yes", "1", "true", "doğru", "var"}


def bip_endeksi(otus: int, kapak_kapali: bool, unutulan: bool, az_kalsin: bool) -> float:
    return (otus * 1.7) + (4.0 if kapak_kapali else 0.0) + (3.14 if unutulan else 0.0) + (5.0 if az_kalsin else 0.0)


def seviye(b: float) -> str:
    if b < 4:
        return "SARI ALARM — komşu henüz duymadı, şebeke ısınıyor"
    if b < 9:
        return "TURUNCU ALARM — site yönetimi haberdar, milli rotor titriyor"
    return "KIRMIZI KESİNTİ — tabak lisanssız santral ilan edildi"


def tutanak(otus: int, kapak_kapali: bool, unutulan: bool, az_kalsin: bool, b: float) -> str:
    simdi = dt.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    satirlar = [
        "=" * 64,
        "T.C. ENERJİ PİYASASI DÜZENLEME KURULU",
        "ÖTMEYİ BIRAKMAYAN MİKRODALGA ŞEBEKESİ TUTANAĞI",
        "=" * 64,
        f"Tutanak saati        : {simdi}",
        f"Ötüş adedi          : {otus}",
        f"Kapak kapalı         : {'EVET — şebeke kilitli' if kapak_kapali else 'HAYIR — geçici açık'}",
        f"Unutulan yemek       : {'EVET — lisanslı yük' if unutulan else 'HAYIR'}",
        f"'Az kalsın açardım'  : {'EVET — ihmal' if az_kalsin else 'HAYIR'}",
        f"Bip Endeksi (B)      : {b:.2f}",
        f"Alarm                : {seviye(b)}",
        "-",
        "Kurul görüşü:",
        random.choice(
            [
                "Bip durmaz. Yurttaş durur.",
                "Kapak bir vanadır. Vana siyaset değildir, tarifedir.",
                "Her ötüş bir kilowatt-saat hatırlatmasıdır.",
                "Tablo dönüyor. Devlet de döner. Fark rotor milidir.",
                "Susmayan fırın, konuşmayan kurumdan daha dürüsttür.",
            ]
        ),
        "-",
        f"Mühür : {MUHUR}",
        f"İmza  : {KAYYUM}",
        f"Tarih : {TARIH}",
        "Ciddi değil. Aynı zamanda ciddi.",
        "=" * 64,
    ]
    return "\n".join(satirlar)


def main() -> int:
    print("T.C. EPDK — Mikrodalga Şebekesi Denetim Terminali")
    print("Patates yok. Siyaset yok. Tarife var.\n")
    try:
        otus_raw = input("Kaç kez öttü? [sayı] ").strip() or "3"
        otus = max(0, int(otus_raw))
    except ValueError:
        print("Sayı değil. Kuruluş üç ötüş varsayar.")
        otus = 3
    kapak = evet_mi(input("Kapak hâlâ kapalı mı? [e/h] "))
    unutulan = evet_mi(input("Yemek içerde unutuldu mu? [e/h] "))
    az = evet_mi(input("Yurttaş 'az kalsın açardım' dedi mi? [e/h] "))

    b = bip_endeksi(otus, kapak, unutulan, az)
    print()
    print(tutanak(otus, kapak, unutulan, az, b))
    print()
    print("Şebekeyi durdurmak için KAPAK yazın. Başka her şey yeni bir ötüştür.")
    komut = input("> ").strip().upper()
    if komut == "KAPAK":
        print("Kapak açıldı. Bip durdu. Geçici. Her kapanış yeni bir açılıştır.")
        print(f"\n{KAYYUM} | {TARIH} | {MUHUR}")
        return 0
    print("KAPAK denmedi. Şebeke ötmeye devam eder.")
    print("BİP. BİP. BİP.")
    print(f"\n{KAYYUM} | {TARIH} | {MUHUR}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
