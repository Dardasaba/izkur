#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/helpers/utils.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import itertools

from typing import Tuple
from collections.abc import Iterable, Iterator

from ..models import Abbreviation, CourtAbbreviation, DecisionsCollection

__all__ = [
    "intervals_extract",
    "intervals_to_str",
    "determine_obj_using_hints",
    "resolve_court",
    "resolve_court_seat",
    "resolve_court_type",
    "resolve_decision_collection",
    "get_obj_from_abbreviation",
]


def intervals_extract(iterable: Iterable[int]) -> Iterator[Tuple[int, int]]:
    iterable = sorted(set(iterable))
    for key, group in itertools.groupby(enumerate(iterable), lambda t: t[1] - t[0]):
        group = list(group)
        yield (group[0][1], group[-1][1])


def intervals_to_str(intervals: list[int]) -> str:
    obj_list: list[str] = []
    for n, m in list(intervals_extract(intervals)):
        if n == m:
            obj_list.append(f"{n}")
        else:
            obj_list.append(f"{n}–{m}")
    return ", ".join(obj_list)


def determine_obj_using_hints(
    obj_list: list[Abbreviation | CourtAbbreviation | DecisionsCollection],
    hints: tuple[
        Abbreviation | str | None, DecisionsCollection | str | None, int | str | None
    ],
) -> Abbreviation | CourtAbbreviation | DecisionsCollection:
    _proceeding_type, _publication, _decision_year = hints
    print(_publication)

    zero_pub = [
        'פ"פ',
        'פל"ע',
        'ש"מ',
        'ש"ע',
        'ס"ע',
        'ס"ק',
        'סב"א',
        'סע"ש',
        'סק"כ',
        'עס"ק',
        'שע"ם',
        'תב"ע',
        'תע"א',
    ]
    one_pub = ['פד"ר', 'תה"ן', 'ה"נ', 'מ"א', "ע'"]
    if isinstance(_publication, str):
        _pub = _publication.split(" ", 1)[0]
        if _pub in one_pub and _pub not in zero_pub:
            return obj_list[1]
        elif _pub in zero_pub and _pub not in one_pub:
            return obj_list[0]
    else:
        if _pub in one_pub and _pub not in zero_pub:
            return obj_list[1]
        elif _pub in zero_pub and _pub not in one_pub:
            return obj_list[0]
    return obj_list[0]


def resolve_court(
    abbreviation: str,
    obj_list: list[DecisionsCollection],
    hints: (
        tuple[
            Abbreviation | str | None,
            DecisionsCollection | str | None,
            int | str | None,
        ]
        | None
    ) = None,
) -> Abbreviation | CourtAbbreviation | DecisionsCollection | None:
    _proceeding_type, _publication, _decision_year = hints
    multiple_courts: dict[str, list] = {}

    rabanical_proceeding_types = ['פד"ר', 'תה"ן', 'ה"נ', 'מ"א', "ע'"]
    labor_proceeding_types = [
        'פ"פ',
        'פל"ע',
        'ש"מ',
        'ש"ע',
        'ס"ע',
        'ס"ק',
        'סב"א',
        'סע"ש',
        'סק"כ',
        'עס"ק',
        'שע"ם',
        'תב"ע',
        'תע"א',
    ]
    labor_publications = []
    rabanical_publications = []
    labor_decision_year = []
    rabanical_decision_year = []

    multiple_courts["אזורי"] = [
        ("בית דין אזורי לעבודה", "בית דין רבני אזורי"),
        (labor_proceeding_types, rabanical_proceeding_types),
        (labor_publications, rabanical_publications),
        (labor_decision_year, rabanical_decision_year),
    ]

    misphat_proceeding_types = []
    din_proceeding_types = []
    misphat_publications = []
    din_publications = []
    mishpat_decision_year = []
    din_decision_year = []

    multiple_courts["ערעורים"] = [
        ("בית הדין הצבאי לערעורים", "בית המשפט הצבאי לערעורים"),
        (misphat_proceeding_types, din_proceeding_types),
        (misphat_publications, din_publications),
        (mishpat_decision_year, din_decision_year),
    ]

    regional_proceeding_types = []
    first_instance_proceeding_types = []
    regional_publications = []
    first_instance_publications = []
    regional_decision_year = []
    first_instance_decision_year = []

    multiple_courts["צבאי"] = [
        ("בית דין צבאי מחוזי", "בית משפט צבאי של ערכאה ראשונה"),
        (regional_proceeding_types, first_instance_proceeding_types),
        (regional_publications, first_instance_publications),
        (regional_decision_year, first_instance_decision_year),
    ]

    obj_list = [e for e in obj_list if e.abbreviation == abbreviation]

    for k in multiple_courts.keys():
        if not obj_list[0].abbreviation == k:
            continue
        data = multiple_courts[k]
        if _proceeding_type in data[1][0]:
            return obj_list[0]
        elif _proceeding_type in data[1][1]:
            return obj_list[1]
        if _publication in data[2][0]:
            return obj_list[0]
        elif _publication in data[2][1]:
            return obj_list[1]
        if _decision_year in data[3][0]:
            return obj_list[0]
        elif _decision_year in data[3][1]:
            return obj_list[1]
    return None


def resolve_court_seat(
    abbreviation: str,
    obj_list: list[DecisionsCollection],
    hints: (
        tuple[
            Abbreviation | str | None,
            DecisionsCollection | str | None,
            int | str | None,
        ]
        | None
    ) = None,
) -> Abbreviation | CourtAbbreviation | DecisionsCollection | None:
    multiple_court_seats = {}
    multiple_court_seats["מר'"] = {("מרכז", "מרכז–לוד"), ([], []), ([], []), ([], [])}
    obj_list = [e for e in obj_list if e.abbreviation == abbreviation]
    if len(obj_list) == 1:
        return obj_list[0]
    elif len(obj_list) > 1:
        if obj_list[0].abbreviation in multiple_court_seats and hints:
            return determine_obj_using_hints(obj_list, hints)
        return obj_list[0]
    return None


def resolve_court_type(
    abbreviation: str,
    obj_list: list[DecisionsCollection],
    hints: (
        tuple[
            Abbreviation | str | None,
            DecisionsCollection | str | None,
            int | str | None,
        ]
        | None
    ) = None,
) -> Abbreviation | CourtAbbreviation | DecisionsCollection | None:

    multiple_court_types = {}
    multiple_court_types['ב"ש'] = {
        ("בקשות שונות", "בקשת שחרור"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['בד"ם'] = {
        (
            "תיק בית דין מיוחד",
            "תיק בית הדין המחוזי למשמעת של לשכת עורכי הדין",
            "תיק בית הדין למשמעת של עובדי המדינה",
        ),
        ([], [], []),
        ([], [], []),
        ([], [], []),
    }
    multiple_court_types['בר"ש'] = {
        ("בקשות רשות ערעור שונות", "בקשת רשות להישפט", "בקשות רישוי"),
        ([], [], []),
        ([], [], []),
        ([], [], []),
    }
    multiple_court_types['ו"ע'] = {
        ("ועדת ערר", "ועדת ערעור"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ע"מ'] = {
        ("ערעור משפחה", "ערעור מיסים"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ע"נ'] = {
        ("ערעור נכים", "ערעור נוער"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['עמ"ם'] = {
        ("ערעור מעצר מנהלי", "ערעור מועצה משפטית"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['עמ"פ'] = {
        ("ערעור מניעת פגישה עם עורך דין", "ערעור על החלטת רשם המפלגות"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['עמ"ש'] = {
        ("ערר מס שבח", "ערעור משפחה"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['עפ"ע'] = {
        ("ערעור פלילי על עדות קטין נפגע עבירה", "ערר בעניין פגישה עם עורך דין"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ער"ם'] = {
        (
            'ערעור לפי חוק הרשויות המקומיות (משמעת), התשל"ח–1978',
            "ערעור על החלטת רשם – מנהלי",
        ),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['עת"ם'] = {
        ("עתירה מנהלית", "ערעור תפיסת מקרקעים"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['רע"ב'] = {
        ("רשות ערעור בתי סוהר", "רשות ערעור על פסק בורר"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ת"א'] = {
        ("תיק אזרחי", "תיק אישות"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ת"ח'] = {
        ("תביעת חפצא", "תיק המנהלה להסדרים במגזר החקלאי"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ת"ק'] = {
        ("תביעות קטנות", "תיק קרקעות"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['ת"ת'] = {
        ("תיק תעבורה", "תיק ביצוע תביעה בהוצאה לפועל"),
        ([], []),
        ([], []),
        ([], []),
    }
    multiple_court_types['תב"כ'] = {
        ("תיק בחירות כלליות", "תיק בחירות לכנסת"),
        ([], []),
        ([], []),
        ([], []),
    }

    obj_list = [e for e in obj_list if e.abbreviation == abbreviation]
    if len(obj_list) == 1:
        return obj_list[0]
    elif len(obj_list) > 1:
        if obj_list[0].abbreviation in multiple_court_types and hints:
            return determine_obj_using_hints(obj_list, hints)
        return obj_list[0]
    return None


def resolve_decision_collection(
    abbreviation: str,
    obj_list: list[DecisionsCollection],
    hints: (
        tuple[
            Abbreviation | str | None,
            DecisionsCollection | str | None,
            int | str | None,
        ]
        | None
    ) = None,
) -> Abbreviation | CourtAbbreviation | DecisionsCollection | None:
    multiple_decision_collections = ["המשפט"]
    obj_list = [e for e in obj_list if e.abbreviation == abbreviation]
    if len(obj_list) == 1:
        return obj_list[0]
    elif len(obj_list) > 1:
        if obj_list[0].abbreviation in multiple_decision_collections and hints:
            return determine_obj_using_hints(obj_list, hints)
        return obj_list[0]
    return None


def get_obj_from_abbreviation(
    abbreviation: str,
    obj_list: list[Abbreviation | CourtAbbreviation | DecisionsCollection],
    hints: (
        tuple[
            Abbreviation | str | None,
            DecisionsCollection | str | None,
            int | str | None,
        ]
        | None
    ) = None,
) -> Abbreviation | CourtAbbreviation | DecisionsCollection | None:
    obj_list = [e for e in obj_list if e.abbreviation == abbreviation]
    if len(obj_list) == 1:
        return obj_list[0]
    elif len(obj_list) > 1:
        if hints:
            return determine_obj_using_hints(obj_list, hints)
        return obj_list[0]
    return None
