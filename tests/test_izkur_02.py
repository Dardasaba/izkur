#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests/test_izkur_02.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from izkur import IsraeliLegislation


def test_02_01_01() -> None:
    s = """חוק איסור נהיגה ברכב בחוף הים, התשנ"ז–1997, ס"ח 84"""
    t = IsraeliLegislation(
        legislation_title="חוק איסור נהיגה ברכב בחוף הים",
        legislation_hebrew_year='התשנ"ז',
        legislation_year=1997,
        legislation_collection='ס"ח',
        first_page_index=84,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_01_02() -> None:
    s = """הצעת חוק החוזים (חלק כללי), התש"ל–1970, ה"ח 129"""
    t = IsraeliLegislation(
        legislation_title="הצעת חוק החוזים (חלק כללי)",
        legislation_hebrew_year='התש"ל',
        legislation_year=1970,
        legislation_collection='ה"ח',
        first_page_index=129,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_01_03() -> None:
    s = """תקנות הנמלים (תיקון מס' 3), התשמ"א–1981, ק"ת 956"""
    t = IsraeliLegislation(
        legislation_title="תקנות הנמלים (תיקון מס' 3)",
        legislation_hebrew_year='התשמ"א',
        legislation_year=1981,
        legislation_collection='ק"ת',
        first_page_index=956,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_01_04() -> None:
    s = """הודעה בדבר קביעת הדרכים והתנאים למינויו של היועץ המשפטי לממשלה, י"פ התש"ס 4894"""
    t = IsraeliLegislation(
        legislation_title="הודעה בדבר קביעת הדרכים והתנאים למינויו של היועץ המשפטי לממשלה",
        legislation_collection='י"פ',
        legislation_collection_year='התש"ס',
        first_page_index=4894,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_02_01() -> None:
    s = """ס' 2 לחוק שכר מינימום, התשמ"ז–1987"""
    t = IsraeliLegislation(
        specific_reference="ס' 2",
        legislation_title="חוק שכר מינימום",
        legislation_hebrew_year='התשמ"ז',
        legislation_year=1987,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_02_02() -> None:
    s = """תק' 3, 5–8 ו-15 לתקנות השבת אבידה, התשל"ג–1973"""
    t = IsraeliLegislation(
        specific_reference="תק' 3, 5–8 ו-15",
        legislation_title="תקנות השבת אבידה",
        legislation_hebrew_year='התשל"ג',
        legislation_year=1973,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_02_03() -> None:
    s = """חלק ג' לתקנות התעבורה, התשכ"א–1961"""
    t = IsraeliLegislation(
        specific_reference="חלק ג'",
        legislation_title="תקנות התעבורה",
        legislation_hebrew_year='התשכ"א',
        legislation_year=1961,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_02_04() -> None:
    s = """פרק ד' לחוק ההוצאה לפועל, התשכ"ז–1967"""
    t = IsraeliLegislation(
        specific_reference="פרק ד'",
        legislation_title="חוק ההוצאה לפועל",
        legislation_hebrew_year='התשכ"ז',
        legislation_year=1967,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


# def test_02_02_05() -> None:
#     s = """סי' א'1 לפרק השני לחלק י' לפקודת מס הכנסה [נוסח חדש]"""
#     t = IsraeliLegislation(
#         specific_reference="סי' א'1 לפרק השני לחלק י'",
#         legislation_title="פקודת מס הכנסה [נוסח חדש]",
#     )
#     assert s == str(t) == str(IsraeliLegislation.from_str(s))


# def test_02_02_06() -> None:
#     s = """פרט 11 לתוספת לחוק למניעת העישון במקומות ציבוריים והחשיפה לעישון, התשמ"ג–1983"""
#     t = IsraeliLegislation(
#         specific_reference="פרט 11 לתוספת",
#         legislation_title="חוק למניעת העישון במקומות ציבוריים והחשיפה לעישון",
#         legislation_hebrew_year='התשמ"ג',
#         legislation_year=1983,
#     )
#     assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_02_07() -> None:
    s = """דברי הסבר להצעת חוק הרשות הלאומית לבטיחות בדרכים, התשס"ו–2005, ה"ח הממשלה 142, 142"""
    t = IsraeliLegislation(
        specific_reference="דברי הסבר",
        legislation_title="הצעת חוק הרשות הלאומית לבטיחות בדרכים",
        legislation_hebrew_year='התשס"ו',
        legislation_year=2005,
        legislation_collection='ה"ח הממשלה',
        first_page_index=142,
        specific_page_index_reference=142,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_03_01() -> None:
    s = """חוק להארכת תוקף של תקנות-שעת-חירום (חוקת השיפוט תש"ח), התש"ט–1949, ס"ח 55"""
    t = IsraeliLegislation(
        legislation_title='חוק להארכת תוקף של תקנות-שעת-חירום (חוקת השיפוט תש"ח)',
        legislation_hebrew_year='התש"ט',
        legislation_year=1949,
        legislation_collection='ס"ח',
        first_page_index=55,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_04_01() -> None:
    s = """חוק העונשין, התשל"ז–1977, ס"ח 226"""
    t = IsraeliLegislation(
        legislation_title="חוק העונשין",
        legislation_hebrew_year='התשל"ז',
        legislation_year=1977,
        legislation_collection='ס"ח',
        first_page_index=226,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_04_02() -> None:
    s = """חוק העונשין (תיקון מס' 39) (חלק מקדמי וחלק כללי), התשנ"ד–1994, ס"ח 348"""
    t = IsraeliLegislation(
        legislation_title="חוק העונשין (תיקון מס' 39) (חלק מקדמי וחלק כללי)",
        legislation_hebrew_year='התשנ"ד',
        legislation_year=1994,
        legislation_collection='ס"ח',
        first_page_index=348,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_05_01() -> None:
    s = """חוק מילווה בטחון, התשל"ג–1973, ס"ח 92"""
    t = IsraeliLegislation(
        legislation_title="חוק מילווה בטחון",
        legislation_hebrew_year='התשל"ג',
        legislation_year=1973,
        legislation_collection='ס"ח',
        first_page_index=92,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_05_02() -> None:
    s = """הודעת המדגמים, התשמ"ט–1989, ק"ת 279"""
    t = IsraeliLegislation(
        legislation_title="הודעת המדגמים",
        legislation_hebrew_year='התשמ"ט',
        legislation_year=1989,
        legislation_collection='ק"ת',
        first_page_index=279,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_05_03() -> None:
    s = """חוק-יסוד: הממשלה, ס"ח התשס"א 158"""
    t = IsraeliLegislation(
        legislation_title="חוק-יסוד: הממשלה",
        legislation_collection='ס"ח',
        legislation_collection_year='התשס"א',
        first_page_index=158,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_05_04() -> None:
    s = """פקודת העיריות [נוסח חדש], נ"ח התשכ"ד 197"""
    t = IsraeliLegislation(
        legislation_title="פקודת העיריות [נוסח חדש]",
        legislation_collection='נ"ח',
        legislation_collection_year='התשכ"ד',
        first_page_index=197,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_07_01() -> None:
    s = """חוק-יסוד: הכנסת, ס"ח התשי"ח 69"""
    t = IsraeliLegislation(
        legislation_title="חוק-יסוד: הכנסת",
        legislation_collection='ס"ח',
        legislation_collection_year='התשי"ח',
        first_page_index=69,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_07_02() -> None:
    s = """חוק-יסוד: נשיא המדינה (תיקון מס' 5), ס"ח התשנ"ט 36"""
    t = IsraeliLegislation(
        legislation_title="חוק-יסוד: נשיא המדינה (תיקון מס' 5)",
        legislation_collection='ס"ח',
        legislation_collection_year='התשנ"ט',
        first_page_index=36,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_07_03() -> None:
    s = """החלטות בדקדוק ובמינוח של האקדמיה ללשון העברית, התשס"ג, י"פ התשס"ד 2278"""
    t = IsraeliLegislation(
        legislation_title="החלטות בדקדוק ובמינוח של האקדמיה ללשון העברית",
        legislation_hebrew_year='התשס"ג',
        legislation_collection='י"פ',
        legislation_collection_year='התשס"ד',
        first_page_index=2278,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))


def test_02_08_01() -> None:
    s = """חוק הירושה, התשכ"ה–1965, ס"ח 63"""
    t = IsraeliLegislation(
        specific_reference=None,
        legislation_title="חוק הירושה",
        legislation_hebrew_year='התשכ"ה',
        legislation_year=1965,
        legislation_collection='ס"ח',
        first_page_index=63,
    )
    assert s == str(t) == str(IsraeliLegislation.from_str(s))
