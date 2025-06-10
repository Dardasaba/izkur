#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/internal_provisions.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import Abbreviation

__all__ = ["INTERNAL_PROVISIONS"]

INTERNAL_PROVISIONS: list[Abbreviation] = []

INTERNAL_PROVISIONS.append(
    Abbreviation(
        title="הוראות הפיקוד העליון",
        abbreviation='הפ"ע',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title='הוראות קבע אכ"א',
        abbreviation='הק"א',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title='הוראות קבע למתקני אכ"א',
        abbreviation='הקמ"א',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title="חוזר מזכירות הפיקוד העליון",
        abbreviation='חוזר מפ"ע',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title='פקודות מטכ"ל',
        abbreviation='פ"מ',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title="פקודת המטה הארצי",
        abbreviation='פקודת המטא"ר',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title="פקודת נציבות בתי הסוהר",
        abbreviation='פקנ"צ',
    )
)
INTERNAL_PROVISIONS.append(
    Abbreviation(
        title="תקן ישראלי",
        abbreviation='ת"י',
    )
)
