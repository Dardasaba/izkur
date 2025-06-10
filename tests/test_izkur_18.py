#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tests/test_izkur_18.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from izkur import IsraeliDecision, COURT_ABBREVIATIONS


def test_18_01_01() -> None:
    s = """בג"ץ 98/69 [bold]ברגמן נ' שר האוצר[/bold], פ"ד כג(1) 693, 698–699 (1969)"""
    t = IsraeliDecision(
        proceeding_type='בג"ץ',
        docket_id="98/69",
        plaintiff="ברגמן",
        respondent="שר האוצר",
        publication='פ"ד',
        volume="כג",
        edition=1,
        first_page_index=693,
        specific_reference=[698, 699],
        decision_year=1969,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_01_02() -> None:
    s = """ד"נ 32/84 [bold]עזבון וויליאמס נ' Israel British Bank (London) (in liquidation)[/bold], פ"ד מד(2) 265, פס' 10 לפסק הדין של השופט ברק (1990)"""
    t = IsraeliDecision(
        proceeding_type='ד"נ',
        docket_id="32/84",
        plaintiff="עזבון וויליאמס",
        respondent="Israel British Bank (London) (in liquidation)",
        publication='פ"ד',
        volume="מד",
        edition=2,
        first_page_index=265,
        specific_reference="פס' 10 לפסק הדין של השופט ברק",
        decision_year=1990,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_01_03() -> None:
    s = """ת"פ (מקומיים י-ם) 2857/85 [bold]מדינת ישראל נ' אורנן[/bold], פ"מ התשמ"ז(ג) 334 (1987)"""
    t = IsraeliDecision(
        proceeding_type='ת"פ',
        court_type="מקומיים",
        court_seat="י-ם",
        docket_id="2857/85",
        plaintiff="מדינת ישראל",
        respondent="אורנן",
        publication='פ"מ',
        volume='התשמ"ז',
        edition="ג",
        first_page_index=334,
        decision_year=1987,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_01_04() -> None:
    s = """תב"ע (אזורי ת"א) מד/708–3 [bold]גולדמן – מדינת ישראל[/bold], פד"ע יח, לח (1986)"""
    t = IsraeliDecision(
        proceeding_type='תב"ע',
        court_type="אזורי",
        court_seat='ת"א',
        docket_id="מד/708–3",
        plaintiff="גולדמן",
        respondent="מדינת ישראל",
        publication='פד"ע',
        volume="יח",
        first_page_index="לח",
        decision_year=1986,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_01() -> None:
    s = """בג"ץ 287/51 [bold]ראם נ' שר האוצר[/bold], פ"ד ח 494 (1954)"""
    t = IsraeliDecision(
        proceeding_type='בג"ץ',
        docket_id="287/51",
        plaintiff="ראם",
        respondent="שר האוצר",
        publication='פ"ד',
        volume="ח",
        first_page_index=494,
        decision_year=1954,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_02() -> None:
    s = """ע"פ 862/80 [bold]מדינת ישראל נ' שבירו[/bold], פ"ד לה(2) 775 (1981)"""
    t = IsraeliDecision(
        proceeding_type='ע"פ',
        docket_id="862/80",
        plaintiff="מדינת ישראל",
        respondent="שבירו",
        publication='פ"ד',
        volume="לה",
        edition=2,
        first_page_index=775,
        decision_year=1981,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_03() -> None:
    s = """ע"א 6821/93 [bold]בנק המזרחי המאוחד בע"מ נ' מגדל כפר שיתופי[/bold], פ"ד מט(4) 221 (1995)"""
    t = IsraeliDecision(
        proceeding_type='ע"א',
        docket_id="6821/93",
        plaintiff='בנק המזרחי המאוחד בע"מ',
        respondent="מגדל כפר שיתופי",
        publication='פ"ד',
        volume="מט",
        edition=4,
        first_page_index=221,
        decision_year=1995,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_04() -> None:
    s = """ע"פ 2910/94 [bold]יפת נ' מדינת ישראל[/bold], פ"ד נ(2) 221 (1996)"""
    t = IsraeliDecision(
        proceeding_type='ע"פ',
        docket_id="2910/94",
        plaintiff="יפת",
        respondent="מדינת ישראל",
        publication='פ"ד',
        volume="נ",
        edition=2,
        first_page_index=221,
        decision_year=1996,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_05() -> None:
    s = """ת"א (שלום פ"ת) 1044/92 [bold]גלזר נ' חוסרבי[/bold], פ"מ התשנ"ט(3) 385 (1999)"""
    t = IsraeliDecision(
        proceeding_type='ת"א',
        court_type="שלום",
        court_seat='פ"ת',
        docket_id="1044/92",
        plaintiff="גלזר",
        respondent="חוסרבי",
        publication='פ"מ',
        volume='התשנ"ט',
        edition=3,
        first_page_index=385,
        decision_year=1999,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_01_06() -> None:
    s = """ה"פ (מחוזי מר') 10–04–30380 [bold]קרפ נ' קרפ[/bold], מקרקעין י/5, 187 (2011)"""
    t = IsraeliDecision(
        proceeding_type='ה"פ',
        court_type="מחוזי",
        court_seat="מר'",
        docket_id="10–04–30380",
        plaintiff="קרפ",
        respondent="קרפ",
        publication="מקרקעין",
        volume="י/5",
        first_page_index=187,
        decision_year=2011,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_02_01() -> None:
    s = """בש"א 1481/96 [bold]נחמני נ' נחמני[/bold], פ"ד מט(5) 598 (1996)"""
    t = IsraeliDecision(
        proceeding_type='בש"א',
        docket_id="1481/96",
        plaintiff="נחמני",
        respondent="נחמני",
        publication='פ"ד',
        volume="מט",
        edition=5,
        first_page_index=598,
        decision_year=1996,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


# def test_18_02_02_02() -> None:
#     s = """בש"א 1481/96 (דנ"א 2401/95) [bold]נחמני נ' נחמני[/bold], פ"ד מט(5) 598 (1996)"""
#     t = IsraeliDecision(
#         proceeding_type='בש"א',
#         docket_id="1481/96",
#         principle_proceeding_type='דנ"א',
#         principle_docket_id="2401/95",
#         plaintiff="נחמני",
#         respondent="נחמני",
#         publication='פ"ד',
#         volume="מט",
#         edition=5,
#         first_page_index=598,
#         decision_year=1996,
#     )
#     assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_02_03() -> None:
    s = """בה"ן 6857/00 [bold]רוטה נ' נצבטייב[/bold], פ"ד נד(4) 707 (2000)"""
    t = IsraeliDecision(
        proceeding_type='בה"ן',
        docket_id="6857/00",
        plaintiff="רוטה",
        respondent="נצבטייב",
        publication='פ"ד',
        volume="נד",
        edition=4,
        first_page_index=707,
        decision_year=2000,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_02_02_04() -> None:
    s = """בה"ן 6857/00א [bold]רוטה נ' נצבטייב[/bold], פ"ד נד(4) 707 (2000)"""
    t = IsraeliDecision(
        proceeding_type='בה"ן',
        docket_id="6857/00א",
        plaintiff="רוטה",
        respondent="נצבטייב",
        publication='פ"ד',
        volume="נד",
        edition=4,
        first_page_index=707,
        decision_year=2000,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_01() -> None:
    s = """בג"ץ 4541/94 [bold]מילר נ' שר הביטחון[/bold], פ"ד מט(4) 94 (1995)"""
    t = IsraeliDecision(
        proceeding_type='בג"ץ',
        docket_id="4541/94",
        plaintiff="מילר",
        respondent="שר הביטחון",
        publication='פ"ד',
        volume="מט",
        edition=4,
        first_page_index=94,
        decision_year=1995,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_02() -> None:
    s = """ת"א (מחוזי ב"ש) 712/87 [bold]נגאוקר נ' דנינו[/bold], פ"מ התשנ"ד(3) 199 (1994)"""
    t = IsraeliDecision(
        proceeding_type='ת"א',
        court_type="מחוזי",
        court_seat='ב"ש',
        docket_id="712/87",
        plaintiff="נגאוקר",
        respondent="דנינו",
        publication='פ"מ',
        volume='התשנ"ד',
        edition=3,
        first_page_index=199,
        decision_year=1994,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_03() -> None:
    s = """בש"א (מחוזי ת"א) 12112/01 [bold]ילין נ' כהן[/bold], פ"מ התשס"א(2) 49 (2002)"""
    t = IsraeliDecision(
        proceeding_type='בש"א',
        court_type="מחוזי",
        court_seat='ת"א',
        docket_id="12112/01",
        plaintiff="ילין",
        respondent="כהן",
        publication='פ"מ',
        volume='התשס"א',
        edition=2,
        first_page_index=49,
        decision_year=2002,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_04() -> None:
    s = """ת"א (שלום י-ם) 12330/92 [bold]קלנג נ' מדינת ישראל[/bold], פ"מ התשנ"ד(4) 177 (1994)"""
    t = IsraeliDecision(
        proceeding_type='ת"א',
        court_type="שלום",
        court_seat="י-ם",
        docket_id="12330/92",
        plaintiff="קלנג",
        respondent="מדינת ישראל",
        publication='פ"מ',
        volume='התשנ"ד',
        edition=4,
        first_page_index=177,
        decision_year=1994,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_05() -> None:
    s = """דיון (אזורי ת"א) ל/370–3 [bold]שטרויכלר – הליגה למלחמה בשחפת[/bold], פד"ע ד, מב (1972)"""
    t = IsraeliDecision(
        proceeding_type="דיון",
        court_type="אזורי",
        court_seat='ת"א',
        docket_id="ל/370–3",
        plaintiff="שטרויכלר",
        respondent="הליגה למלחמה בשחפת",
        publication='פד"ע',
        volume="ד",
        first_page_index="מב",
        decision_year=1972,
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


def test_18_03_06() -> None:
    s = """ת' (אזורי ת"א) 1557/תשי"ג [bold]חברת "יינות אליעז" בע"מ נ' חברת "אשכול ענבים"[/bold], פד"ר א 178 (התשי"ג)"""
    t = IsraeliDecision(
        proceeding_type="ת'",
        court_type=COURT_ABBREVIATIONS[2],
        court_seat='ת"א',
        docket_id='1557/תשי"ג',
        plaintiff='חברת "יינות אליעז" בע"מ',
        respondent='חברת "אשכול ענבים"',
        publication='פד"ר',
        volume="א",
        first_page_index=178,
        decision_year='התשי"ג',
    )
    assert s == str(t) == str(IsraeliDecision.from_str(s))


# def test_18_03_07() -> None:
#     s = """ע/212/99 (ערעורים צה"ל) [bold]קלמקוב נ' התובע הצבאי הראשי[/bold], פד"צ 1999, 336 (2000)"""

# def test_18_03_08() -> None:
#     s = """עד"י (ערעורים איו"ש) 56/00 [bold]קוואסמה נ' התובע הצבאי[/bold], פש"מ יא 48 (2000)"""

# def test_18_03_09() -> None:
#     s = """ה"פ (כלכלית ת"א) 11–09–18318 [bold]סרגוסי נ' וויקספרס בע"מ[/bold], תאגידים ח/4, 526 (2011)"""

# def test_18_03_10() -> None:
#     s = """תמ"ש (משפחה כ"ס) 5170/01 [bold]נסיראת נ' נסיראת[/bold], פ"מ משפחה התשס"א 687 (2003)"""

# def test_18_03_11() -> None:
#     s = """דב"ע (ארצי) נז/1–7 [bold]ליס – קופת חולים הכללית[/bold], פד"ע לב 477 (1997)"""

# def test_18_03_12() -> None:
#     s = """עב"ל (ארצי) 338/96 [bold]המוסד לביטוח לאומי – עובדיה[/bold], פד"ע לו 213 (2000)"""

# def test_18_03_13() -> None:
#     s = """ע' (גדול) תשל"ב/144 [bold]המועצה הדתית תל-אביב–יפו נ' א'[/bold], פד"ר י 38 (התשל"ה)"""

# def test_18_03_14() -> None:
#     s = """ת"א (ימאות) 845/71 [bold]"ט. פורט (רוטרדם) ב.ו." חברה הולנדית ליבוא וליצוא פרי הדר נ' "בת סנפיר" קווי ים התיכון בע"מ[/bold], פ"מ התשל"ו(1) 27 (1975)"""

# def test_18_03_15() -> None:
#     s = """ה"ע (הגבלים עסקיים) 9/97 [bold]בזק בינלאומי בע"מ נ' הממונה על ההגבלים העסקיים[/bold], פ"מ התשנ"ט(1) 241 (2000)"""

# def test_18_03_16() -> None:
#     s = """ע"ש (מים) 103/01 [bold]איגוד ערים איילון (ביוב ביעור יתושים וסילוק אשפה) נ' נציב המים משרד התשתיות הלאומיות[/bold], פ"מ התש"ס(2) 273 (2001)"""
