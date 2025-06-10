#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/decisions_collections.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import DecisionsCollection

__all__ = ["DECISIONS_COLLECTIONS"]

DECISIONS_COLLECTIONS: list[DecisionsCollection] = []

DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Annotated Law Reports",
        abbreviation="ALR",
        mandatory=True,
        description="בית המשפט העליון",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Current Law Reports",
        abbreviation="CLR",
        mandatory=True,
        description="בית המשפט העליון",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Collection of Judgements",
        abbreviation="COJ",
        mandatory=True,
        description="מכל בתי המשפט",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Haifa Law Reports",
        abbreviation="HLR",
        mandatory=True,
        description="בית המשפט העליון",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Northern Law Reports",
        abbreviation="NLR",
        mandatory=True,
        description="בתי משפט מחוזיים",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Law Reports of Palestine",
        abbreviation="PLR",
        mandatory=True,
        description="מועצת המלך ובית המשפט העליון",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Selected Cases of the District Courts",
        abbreviation="SCDC",
        mandatory=True,
        description="בתי משפט מחוזיים",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Annotated Supreme Court Judgements",
        abbreviation="SCJ",
        mandatory=True,
        description="בית המשפט העליון",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="Law Reports of the District of Tel-Aviv",
        abbreviation="TALR",
        mandatory=True,
        description="בתי משפט מחוזיים",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="אוסף פסקי דין נבחרים של בית המשפט העליון",
        abbreviation='אפ"ן',
        mandatory=True,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="הלכות מסים", abbreviation='ה"מ', mandatory=False, description=""
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="קובץ פסקי דין של בתי המשפט המחוזיים",
        abbreviation="המשפט",
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="קובץ פסקי דין של בתי המשפט המחוזיים",
        abbreviation="המשפט",
        mandatory=True,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין בעניני שכירות בהוצאת א' מאירי",
        abbreviation="מאירי",
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="תקציר פסקי דין של בית המשפט העליון בעריכת נח סביר",
        abbreviation="סביר",
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי-דין של בית המשפט העליון",
        abbreviation='פ"ד',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title='"פסקים" של בתי המשפט המחוזיים ובתי משפט השלום',
        abbreviation='פ"מ',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title='תמציות של פסקים של בתי המשפט. צורפו בסוף כרכי "פסקים"',
        abbreviation='פ"מ (ת)',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title='"פסקים" של בתי המשפט לענייני משפחה',
        abbreviation='פ"מ משפחה',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title='"פסקים" של בית המשפט העליון',
        abbreviation='פ"ע',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין של בתי הדין לביטוח לאומי",
        abbreviation='פב"ל',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין אזרחיים", abbreviation='פד"א', mandatory=False, description=""
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין של בית הדין הצבאי לערעורים כערכאת ערעור על בתי המשפט הצבאיים לפי תקנות ההגנה (שעות חירום), 1945",
        abbreviation='פד"ה',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין בעניינים מנהליים",
        abbreviation='פד"מ',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין של בתי הדין לעבודה",
        abbreviation='פד"ע',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין נבחרים של בית הדין הצבאי לערעורים",
        abbreviation='פד"צ',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין של בתי הדין הרבניים",
        abbreviation='פד"ר',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין משמעתיים של לשכת עורכי הדין",
        abbreviation='פדי"מ',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין בעניני מסים בהוצאת לשכת רואי החשבון",
        abbreviation='פדמ"ס',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין של בתי המשפט הצבאיים",
        abbreviation='פצ"ן',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="פסקי דין נבחרים של בתי המשפט הצבאיים בשטחים המוחזקים",
        abbreviation='פש"מ',
        mandatory=False,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="אוסף פסקי דין של בית המשפט המחוזי בתל-אביב",
        abbreviation='פת"א',
        mandatory=True,
        description="",
    )
)
DECISIONS_COLLECTIONS.append(
    DecisionsCollection(
        title="קובץ פסקי דין אזרחיים",
        abbreviation='קפ"ד',
        mandatory=False,
        description="",
    )
)
