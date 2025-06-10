#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/legislation_collections.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import Abbreviation

__all__ = ["LEGISLATION_COLLECTIONS"]

LEGISLATION_COLLECTIONS: list[Abbreviation] = []

LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="Palestine Gazette",
        abbreviation="P.G.",
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="Supplement",
        abbreviation="Supp.",
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="הצעות חוק",
        abbreviation='ה"ח',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="הצעות חוק  – הכנסת",
        abbreviation='ה"ח הכנסת',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="הצעות חוק  – הממשלה",
        abbreviation='ה"ח הממשלה',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="דיני מדינת ישראל – הצעות נוסח חדש",
        abbreviation='הנ"ח',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="חוקי תקציב",
        abbreviation='ח"ת',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="חוקי תקציב – הצעות",
        abbreviation='ח"ת הצעות',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="חוקי ארץ ישראל",
        abbreviation='חא"י',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="ילקוט הפרסומים",
        abbreviation='י"פ',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="כתבי אמנה",
        abbreviation='כ"א',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="דיני מדינת ישראל – נוסח חדש",
        abbreviation='נ"ח',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="ספר החוקים",
        abbreviation='ס"ח',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="עתון רשמי",
        abbreviation='ע"ר',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="קובץ התקנות",
        abbreviation='ק"ת',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="קובץ התקנות – חיקוקי שלטון מקומי",
        abbreviation='ק"ת חש"ם',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="קובץ התקנות – שיעורי מכס, מס קניה ותשלומי חובה",
        abbreviation='ק"ת – שיעורי מק"ח',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="קובץ מנשרים, צווים ומינויים",
        abbreviation='קמצ"ם',
    )
)
LEGISLATION_COLLECTIONS.append(
    Abbreviation(
        title="תוספת (לעתון הרשמי)",
        abbreviation="תוס'",
    )
)
