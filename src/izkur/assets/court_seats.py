#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/court_seats.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import Abbreviation

__all__ = ["COURT_SEATS"]

COURT_SEATS: list[Abbreviation] = []

COURT_SEATS.append(Abbreviation(title="אור יהודה", abbreviation='א"י'))
COURT_SEATS.append(Abbreviation(title="אילת", abbreviation="אי'"))
COURT_SEATS.append(Abbreviation(title="אריאל", abbreviation="אר'"))
COURT_SEATS.append(Abbreviation(title="אשקלון", abbreviation="אש'"))
COURT_SEATS.append(Abbreviation(title="אשדוד", abbreviation="אשד'"))
COURT_SEATS.append(Abbreviation(title="בת ים", abbreviation='ב"י'))
COURT_SEATS.append(Abbreviation(title="באר שבע", abbreviation='ב"ש'))
COURT_SEATS.append(Abbreviation(title="בית שמש", abbreviation='בי"ש'))
COURT_SEATS.append(Abbreviation(title="בית שאן", abbreviation='ביש"א'))
COURT_SEATS.append(Abbreviation(title="דימונה", abbreviation="די'"))
COURT_SEATS.append(Abbreviation(title="הרצליה", abbreviation="הר'"))
COURT_SEATS.append(Abbreviation(title="חדרה", abbreviation="חד'"))
COURT_SEATS.append(Abbreviation(title="חולון", abbreviation="חו'"))
COURT_SEATS.append(Abbreviation(title="חיפה", abbreviation="חי'"))
COURT_SEATS.append(Abbreviation(title="טול כרם", abbreviation='ט"כ'))
COURT_SEATS.append(Abbreviation(title="טבריה", abbreviation="טב'"))
COURT_SEATS.append(Abbreviation(title="ירושלים", abbreviation="י-ם"))
COURT_SEATS.append(Abbreviation(title="כפר סבא", abbreviation='כ"ס'))
COURT_SEATS.append(Abbreviation(title="מסעדה", abbreviation="מס'"))
COURT_SEATS.append(Abbreviation(title="מרכז", abbreviation="מר'"))
COURT_SEATS.append(Abbreviation(title="מרכז–לוד", abbreviation="מר'"))
COURT_SEATS.append(Abbreviation(title="נהריה", abbreviation="נה'"))
COURT_SEATS.append(Abbreviation(title="נצרת", abbreviation="נצ'"))
COURT_SEATS.append(Abbreviation(title="נתניה", abbreviation="נת'"))
COURT_SEATS.append(Abbreviation(title="עפולה", abbreviation="עפ'"))
COURT_SEATS.append(Abbreviation(title="פתח תקוה", abbreviation='פ"ת'))
COURT_SEATS.append(Abbreviation(title="קריית ביאליק", abbreviation='ק"ב'))
COURT_SEATS.append(Abbreviation(title="קריית גת", abbreviation='ק"ג'))
COURT_SEATS.append(Abbreviation(title="קריית שמונה", abbreviation='ק"ש'))
COURT_SEATS.append(Abbreviation(title="קצרין", abbreviation="קצ'"))
COURT_SEATS.append(Abbreviation(title="קריות", abbreviation="קר'"))
COURT_SEATS.append(Abbreviation(title="רמת גן", abbreviation='ר"ג'))
COURT_SEATS.append(Abbreviation(title="רמת הגולן", abbreviation='ר"ה'))
COURT_SEATS.append(Abbreviation(title="ראשון לציון", abbreviation='ראשל"צ'))
COURT_SEATS.append(Abbreviation(title="רחובות", abbreviation="רח'"))
COURT_SEATS.append(Abbreviation(title="רמלה", abbreviation="רמ'"))
COURT_SEATS.append(Abbreviation(title="תל אביב–יפו", abbreviation='ת"א'))
