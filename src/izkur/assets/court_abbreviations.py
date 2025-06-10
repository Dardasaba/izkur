#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/court_abbreviations/__init__.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import CourtAbbreviation

__all__ = ["COURT_ABBREVIATIONS"]

COURT_ABBREVIATIONS: list[CourtAbbreviation] = []

COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית המשפט העליון",
        abbreviation="",
        indicate_seat=False,
        indicate_title=False,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית דין אזורי לעבודה",
        abbreviation="אזורי",
        indicate_seat=True,
        indicate_title=True,
        separator="–",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית דין רבני אזורי",
        abbreviation="אזורי",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין הארצי לעבודה",
        abbreviation="ארצי",
        indicate_seat=False,
        indicate_title=True,
        separator="–",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין הרבני הגדול",
        abbreviation="גדול",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין להגבלים עסקיים",
        abbreviation="הגבלים עסקיים",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="ההוצאה לפועל",
        abbreviation='הוצל"פ',
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין לחוזים אחידים",
        abbreviation="חוזים אחידים",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין לימאות",
        abbreviation="ימאות",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="המחלקה הכלכלית",
        abbreviation="כלכלית",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title='בית הדין לעררים לפי חוק הכניסה לישראל, התשי"ב–1952',
        abbreviation="כניסה לישראל",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית המשפט המחוזי",
        abbreviation="מחוזי",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין לענייני מים",
        abbreviation="מים",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לעניינים מנהליים",
        abbreviation="מנהליים",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לעניינים מקומיים",
        abbreviation="מקומיים",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין לביקורת משמורת של שוהים שלא כדין",
        abbreviation="משמורת שוהים",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין המחוזי למשמעת של לשכת עורכי הדין",
        abbreviation='משמעת עו"ד',
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין הארצי למשמעת של לשכת עורכי הדין",
        abbreviation='משמעת עו"ד ארצי',
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין למשמעת של עובדי מדינה",
        abbreviation="משמעת עובדי המדינה",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין למשמעת לשופטים",
        abbreviation="משמעת שופטים",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לענייני משפחה",
        abbreviation="משפחה",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לנוער",
        abbreviation="נוער",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין הצבאי לערעורים",
        abbreviation="ערעורים",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית המשפט הצבאי לערעורים",
        abbreviation="ערעורים",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית דין צבאי מחוזי",
        abbreviation="צבאי",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט צבאי של ערכאה ראשונה",
        abbreviation="צבאי",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לשכירות",
        abbreviation="שכירות",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט השלום",
        abbreviation="שלום",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לתביעות קטנות",
        abbreviation="תביעות קטנות",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית הדין לתחרות",
        abbreviation="תחרות",
        indicate_seat=False,
        indicate_title=True,
        separator="נ'",
    )
)
COURT_ABBREVIATIONS.append(
    CourtAbbreviation(
        title="בית משפט לתעבורה",
        abbreviation="תעבורה",
        indicate_seat=True,
        indicate_title=True,
        separator="נ'",
    )
)
