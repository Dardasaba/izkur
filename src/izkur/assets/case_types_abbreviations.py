#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/case_types_abbreviations.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import Abbreviation

__all__ = ["CASE_TYPES_ABBREVIATIONS"]

CASE_TYPES_ABBREVIATIONS: list[Abbreviation] = []

CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אישור בחירות", abbreviation='א"ב'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אישור מפלגות", abbreviation='א"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אישור צוואה", abbreviation='א"צ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="איחוד תובענות", abbreviation='א"ת'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק אזרחי", abbreviation="א'"))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אבעיה", abbreviation="אבע'"))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אימוץ", abbreviation='אמ"ץ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="אכיפת פסק חוץ", abbreviation='אפ"ח')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="אפוטרופסות", abbreviation="אפ'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="איחוד תיקים פליליים", abbreviation='את"פ')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ביטוח לאומי", abbreviation='ב"ל'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ברירת קנס", abbreviation='ב"ק'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="בקשות שונות", abbreviation='ב"ש'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="בקשת שחרור", abbreviation='ב"ש'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לאיסור פרסום שם חשוד", abbreviation='בא"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לביטול איסור שימוש", abbreviation='בא"ש')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="בקשות בנייה", abbreviation='בב"ן'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בית משפט גבוה לצדק", abbreviation='בג"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="תיק בית הדין הארצי למשמעת של לשכת עורכי הדין", abbreviation='בד"א'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בית דין מיוחד", abbreviation='בד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="תיק בית הדין המחוזי למשמעת של לשכת עורכי הדין", abbreviation='בד"ם'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בית הדין למשמעת של עובדי המדינה", abbreviation='בד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בית דין משמעתי לשופטים", abbreviation='בדמ"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת התרת נישואין", abbreviation='בה"ן')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה להיתר עיון", abbreviation='בה"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת היתר טיפול רפואי", abbreviation='בהט"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת חשיפת זהות", abbreviation='בח"ז')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בית דין מיוחד", abbreviation='ביד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות עירייה אחרות", abbreviation='בע"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לעיון בחומר חקירה", abbreviation='בע"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת רשות ערעור משפחה", abbreviation='בע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לאישור עיקול", abbreviation='בע"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לביטול פסילה מנהלית", abbreviation='בפ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לפסילה עד תום ההליכים", abbreviation='בפ"ת')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לצו אינטרנט", abbreviation='בצ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ביטול צו הריסה מנהלי", abbreviation='בצה"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ביטול קנס מנהלי", abbreviation='בק"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת רשות ערעור מנהלי", abbreviation='בר"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת רשות ערעור ברכב", abbreviation='בר"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות רשות ערעור שונות", abbreviation='בר"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת רשות להישפט", abbreviation='בר"ש')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="בקשות רישוי", abbreviation='בר"ש'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות שונות אזרחי", abbreviation='בש"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לשחזור תיק", abbreviation='בש"ז')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות שונות מנהלי", abbreviation='בש"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לשחרור בערובה", abbreviation='בש"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות שונות פלילי", abbreviation='בש"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשות שונות בבית המשפט הגבוה לצדק", abbreviation='בשג"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לתשלום תכוף", abbreviation='בת"ת')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="גישור פלילי", abbreviation='ג"פ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="גילוי ראיה", abbreviation='ג"ר'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעות לפי חוק הגזזת", abbreviation="גזז'")
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="גרימת מוות בנהיגה רשלנית", abbreviation='גמ"ר')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="דמי חבר", abbreviation='ד"ח'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק דמי טיפול ארגוני", abbreviation='ד"ט')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="דיון מהיר", abbreviation='ד"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="דיון נוסף", abbreviation='ד"נ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון בית דין ארצי לעבודה", abbreviation='דב"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון מהיר בסמכות רשם", abbreviation='דמ"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון מהיר בסמכות שופט", abbreviation='דמ"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון נוסף אזרחי", abbreviation='דנ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון נוסף מנהלי", abbreviation='דנ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון נוסף פלילי", abbreviation='דנ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="דיון נוסף בבית המשפט הגבוה לצדק", abbreviation='דנג"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="העברת מקום דיון", abbreviation='ה"ד')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="הטרדה מאיימת וצו הגנה", abbreviation='ה"ט')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק הסדר כובל", abbreviation='ה"כ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="היתר נישואין", abbreviation='ה"נ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="הגבלים עסקיים", abbreviation='ה"ע'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="המרצת פתיחה", abbreviation='ה"פ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="החזרת תפוס", abbreviation='ה"ת'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="העברת מקום דיון – פלילי", abbreviation='הד"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="העברת מקום דיון / איחוד תיקים", abbreviation='המ"ד')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="הארכת מעצר", abbreviation='המ"ע'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="הארכת מועד להישפט", abbreviation='המ"ש')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="המרצה", abbreviation="המ'"))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="האזנת סתר", abbreviation='הס"ת'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="העסקת עובדים זרים", abbreviation='הע"ז')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="המרצת פתיחה בוררות", abbreviation='הפ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה להארכת פסילה מנהלית", abbreviation='הפ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="הצהרת מוות", abbreviation='הצ"ם'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="השגת מזכירות אזרחי", abbreviation='הש"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="השגת מזכירות מנהלי", abbreviation='הש"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="השגת מזכירות פלילי", abbreviation='הש"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='השגת מזכירות בג"ץ', abbreviation='השג"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="התפרעות בבית משפט", abbreviation='הת"ב')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ועדת היתרים", abbreviation='ו"ה'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ועדת ערר", abbreviation='ו"ע'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ועדת ערעור", abbreviation='ו"ע'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ביטול קנס לפי חוק ועדות חקירה", abbreviation='וח"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ועדת שחרורים מיוחדת", abbreviation='וש"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ועדת שחרורים קציבה", abbreviation='וש"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ועדת שחרורים רגילה", abbreviation='וש"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ועדת שחרורים קציבה מורשעים", abbreviation='ושק"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ועדת שחרורים נוער", abbreviation='ושר"ן')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="חוזה אחיד", abbreviation='ח"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="חיקור דין", abbreviation='ח"ד'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק חנייה", abbreviation='ח"נ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעות מכוח חוקים שונים", abbreviation='ח"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק חוק ביטוח בריאות ממלכתי", abbreviation='חב"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חיקור דין אזרחי", abbreviation='חד"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חיקור דין משפחה", abbreviation='חד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חיקור דין פלילי", abbreviation='חד"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חדלות פירעון של יחיד", abbreviation='חדל"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חדלות פירעון תאגיד", abbreviation='חדל"ת')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='בקשה לפי חוק להגנה על עדים, התשס"ט–2008', abbreviation='חה"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חקירת סיבות מוות", abbreviation='חס"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חוקי עזר עירוניים – בררת משפט", abbreviation='חע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="חוקי עזר עירוניים – בררת קנס", abbreviation='חע"ק')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="יישוב סכסוך", abbreviation='י"ס'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="הוצאה לפועל – יהודה והשומרון", abbreviation='יו"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="כפיית ציות בית דין דתי", abbreviation='כ"צ')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מעמד אישי", abbreviation='מ"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="משפט חוזר", abbreviation='מ"ח'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מעצר ימים", abbreviation='מ"י'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="צו מעצר כללי", abbreviation='מ"כ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מעצר מנהלי", abbreviation='מ"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מינוי סנגור", abbreviation='מ"ס'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מסמך פלילי", abbreviation='מ"פ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מעצר עד תום ההליכים", abbreviation='מ"ת')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מעצרים", abbreviation="מ'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מבנים מסוכנים", abbreviation='מב"ס')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מגבלת חזרת עבריין מין", abbreviation='מח"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מעצר ימים בהעדר", abbreviation='מי"ב')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מסירת מסמכים", abbreviation='ממ"ס'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מינוי סנגור טרם משפט", abbreviation='מס"ט')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מעצר ימים", abbreviation='מע"י'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מאסר – קנס מנהלי", abbreviation='מק"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תאונת דרכים ללא נפגעי גוף", abbreviation='נ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="מניעת מפגש", abbreviation='נ"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="נזקקות", abbreviation="נ'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תאונת דרכים ללא נפגעי גוף אדום", abbreviation='נב"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לנשיאת מאסר בישראל", abbreviation='נמ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ניהול רכושם של נעדרים או שבויים", abbreviation='נע"ד')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="נוער", abbreviation="נער"))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="סכסוך עבודה", abbreviation='ס"ע'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="סכסוך קיבוצי", abbreviation='ס"ק'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעות בין ארגוניות", abbreviation='סב"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="סכסוך עבודה בסמכות שופט", abbreviation='סע"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="סכסוך קיבוצי כללי (בין ארגון עובדים לארגון מעבידים)", abbreviation='סק"כ'
    )
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור אזרחי", abbreviation='ע"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור בחירות", abbreviation='ע"ב'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת ועדה", abbreviation='ע"ו')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערר אחר", abbreviation='ע"ח'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק כספי – עליון", abbreviation='ע"ל')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור משפחה", abbreviation='ע"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור מיסים", abbreviation='ע"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור נכים", abbreviation='ע"נ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור נוער", abbreviation='ע"נ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור עבודה", abbreviation='ע"ע'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור פלילי", abbreviation='ע"פ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על החלטת קצין", abbreviation='ע"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת רשם", abbreviation='ע"ר')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור שונה", abbreviation='ע"ש'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור", abbreviation="ע'"))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור אחר", abbreviation='עא"ח'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בעניין איסור פרסום", abbreviation='עא"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור בזיון בית משפט", abbreviation='עב"ז')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על בית דין למשמעת", abbreviation='עב"י')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור ביטוח לאומי", abbreviation='עב"ל')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בדיקה פסיכיאטרית", abbreviation='עב"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בית הדין לעבודה", abbreviation="עב'")
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על בקשה לאיסור פרסום שם חשוד", abbreviation='עבא"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="ערעור לבית הדין הצבאי לערעורים מבית המשפט הצבאי (לפי תקנות ההגנה (שעת חירום), 1945)",
        abbreviation='עבמ"ץ',
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על בקשת עיון בחומר חקירה", abbreviation='עבע"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עתירה לגילוי ראיה", abbreviation='עג"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור דן יחיד", abbreviation='עד"י')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור דיון מהיר", abbreviation='עד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר הגנת הציבור מפני עברייני מין", abbreviation='עה"ג')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור הסגרה", abbreviation='עה"ס'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לביטול עונש שהוטל בשל הפרעה", abbreviation='עה"פ')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="עיזבון", abbreviation="עז'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עיון חוזר בעניין כלכלי", abbreviation='עח"כ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בעניין חילוט ערבויות", abbreviation='עח"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='ערר על פי חוק המים, התשי"ט–1959', abbreviation='עח"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בעניין חילוט רכוש", abbreviation='עח"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור חדלות פירעון", abbreviation='עחד"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור חוק האזנות סתר", abbreviation='עחה"ס')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר עיכוב ביצוע", abbreviation='עכ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על פי חוק", abbreviation='על"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור לשכת עורכי הדין", abbreviation='על"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עניינים מקומיים אחרים", abbreviation='עמ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור מס הכנסה", abbreviation='עמ"ה')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='ערעור לפי חוק משפחות חיילים שנספו במערכה (תגמולים ושיקום), התש"י–1950',
        abbreviation='עמ"ח',
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר מעצר ימים", abbreviation='עמ"י')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור מעצר מנהלי", abbreviation='עמ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור מועצה משפטית", abbreviation='עמ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור מנהלי", abbreviation='עמ"ן'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור מניעת פגישה עם עורך דין", abbreviation='עמ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת רשם המפלגות", abbreviation='עמ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור משפחה אימוץ", abbreviation='עמ"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עניינים מקומיים", abbreviation='עמ"ק')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערר מס שבח", abbreviation='עמ"ש'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="ערעור משפחה", abbreviation='עמ"ש'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר מעצר עד תום ההליכים", abbreviation='עמ"ת')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="ערעור על בית דין משמעתי של לשכת עורכי הדין", abbreviation='עמל"ע'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="ערעור על בית דין משמעתי של רשויות מקומיות", abbreviation='עמר"ם'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על בית דין משמעתי של עובדי המדינה", abbreviation='עמש"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור נוער אזרחי", abbreviation='ענ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על מניעת מפגש", abbreviation='ענ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור נוער פלילי", abbreviation='ענ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עניין מנהלי אחר", abbreviation='ענמ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור נושאי משרה שלטונית", abbreviation='ענמ"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור סכסוך קיבוצי", abbreviation='עס"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור עתירת אסיר", abbreviation='עע"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור עתירה מנהלית", abbreviation='עע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בעניין עיון בראיות התביעה", abbreviation='עע"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור עתירת אסיר", abbreviation='עעת"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי אחר", abbreviation='עפ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי – גזר דין", abbreviation='עפ"ג')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על פסילה מנהלית", abbreviation='עפ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על פסילת רישיון", abbreviation='עפ"ן')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פסלות שופט", abbreviation='עפ"ס')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי על עדות קטין נפגע עבירה", abbreviation='עפ"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר בעניין פגישה עם עורך דין", abbreviation='עפ"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי רצח", abbreviation='עפ"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי תעבורה", abbreviation='עפ"ת')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי אחר עדות קטין נפגע עבירה", abbreviation='עפא"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי גזר דין עדות קטין נפגע עבירה", abbreviation='עפג"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פלילי על בית משפט לעניינים מקומיים", abbreviation='עפמ"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור פסלות שופט – פלילי", abbreviation='עפס"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על צו מניעה – סגירה מנהלית לעסק", abbreviation='עצ"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערר על גובה קנס מנהלי", abbreviation='עק"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='ערעור על קובלנה פלילית ע"י הנאשם', abbreviation='עק"ן')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='ערעור על קובלנה פלילית ע"י הקובל', abbreviation='עק"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת רשם – אזרחי", abbreviation='ער"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='ערעור לפי חוק הרשויות המקומיות (משמעת), התשל"ח–1978', abbreviation='ער"ם'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת רשם – מנהלי", abbreviation='ער"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת רשם – פלילי", abbreviation='ער"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='ערעור על החלטת רשם – בג"ץ', abbreviation='ערג"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור שונה אזרחי", abbreviation='עש"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור משמעתי בעניין עובדי שירות המדינה", abbreviation='עש"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור על החלטת שר העבודה והרווחה", abbreviation='עש"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור שירות התעסוקה", abbreviation='עש"ת')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק עתירות אסירים", abbreviation='עת"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='ערר על תפיסת חפצים (לפי סעיף 38א לפקודת סדר הדין הפלילי (מעצר וחיפוש) [נוסח חדש], התשכ"ט–1969)',
        abbreviation='עת"ח',
    )
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="עתירה מנהלית", abbreviation='עת"ם'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור תפיסת מקרקעים", abbreviation='עת"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="ערעור תיק פלילי בנייה", abbreviation='עתפ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="פרטי אירוע", abbreviation='פ"א'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פסק דין הצהרתי", abbreviation='פ"ה')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="פשע חמור", abbreviation='פ"ח'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="פסילת מועמד", abbreviation='פ"מ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פיצויי פיטורין", abbreviation='פ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="פניית תעבורה", abbreviation='פ"ת'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק פלילי", abbreviation="פ'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק עבירות תעבורה חמורות אדום", abbreviation='פל"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פיצויים לעובדים", abbreviation='פל"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="עבירות תעבורה חמורות", abbreviation="פל'")
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פסילת משרד רישוי", abbreviation='פמ"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פיקוח על עבריין מין", abbreviation='פע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="פיקוח וחוקים אחרים", abbreviation="פקח'")
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק פירוקים", abbreviation='פר"ק'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="איסור פרסום", abbreviation="פר'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשה לשחזור תיק פלילי", abbreviation='פש"ז')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="פשיטת רגל", abbreviation='פש"ר'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="צו אחר", abbreviation='צ"א'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='צו הריסה ללא הרשעה (לפי סעיף 212 לחוק התכנון הבניה התשכ"ה–1965)',
        abbreviation='צ"ה',
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="צו עשה / צו מניעה (קבועים)", abbreviation='צ"ו')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="צו חיפוש / צו כניסה", abbreviation='צ"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="צו מניעה – סגירה מנהלית לעסק", abbreviation='צ"מ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="צו ביניים לנזקקות", abbreviation='צב"ן')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="קופת גמל אזרחי", abbreviation='ק"ג')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="קבלת מידע", abbreviation='ק"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="קובלנה פלילית", abbreviation='ק"פ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="רשות ערעור", abbreviation='ר"ע'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור חדלות פירעון", abbreviation='רחד"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור משפחה", abbreviation='רמ"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור אזרחי", abbreviation='רע"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור בתי סוהר", abbreviation='רע"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור על פסק בורר", abbreviation='רע"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור על ועדה", abbreviation='רע"ו')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור מנהלי", abbreviation='רע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק רישוי עסקים", abbreviation='רע"ס')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור פלילי", abbreviation='רע"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור על החלטת ראש הוצאה לפועל", abbreviation='רע"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="רשות ערעור על החלטת רשם המרכז לגביית קנסות, אגרות והוצאות",
        abbreviation='רע"ר',
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור שונה", abbreviation='רע"ש')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור פיקוח אלקטרוני", abbreviation='רעפ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור על החלטת רשם ההוצאה לפועל", abbreviation='רער"ץ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור עתירת אסיר", abbreviation='רעת"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='בקשת רשות לערור על תפיסת חפצים (לפי סעיף 38א לפקודת סדר הדין הפלילי (מעצר וחיפוש) [נוסח חדש], התשכ"ט–1969)',
        abbreviation='רעת"ח',
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור על הוצאה לפועל", abbreviation='רצ"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="רשות ערעור תביעות קטנות", abbreviation='רת"ק')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="שכר מינימום", abbreviation='ש"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="שכר עבודה", abbreviation='ש"ע'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="שחרור בערובה בהחלטת קצין", abbreviation='ש"ק')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="שינוי שם", abbreviation='ש"ש'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="שכירות", abbreviation="ש'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת שופט בעל דין בהליך", abbreviation='שב"ד')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="בקשת שופט נאשם", abbreviation='שנ"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="שעות עבודה ומנוחה", abbreviation='שע"ם')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק אזרחי", abbreviation='ת"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק אישות", abbreviation='ת"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעת בוררות", abbreviation='ת"ב'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק קביעת גיל", abbreviation='ת"ג'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תאונת דרכים", abbreviation='ת"ד'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעת חפצא", abbreviation='ת"ח'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק המנהלה להסדרים במגזר החקלאי", abbreviation='ת"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק התנגדות לביצוע שטר", abbreviation='ת"ט')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תחרות כלכלית", abbreviation='ת"כ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תובענה מנהלית", abbreviation='ת"מ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק עיזבונות", abbreviation='ת"ע'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק פלילי", abbreviation='ת"פ'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תובענה ייצוגית", abbreviation='ת"צ')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעות קטנות", abbreviation='ת"ק'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק קרקעות", abbreviation='ת"ק'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק תעבורה", abbreviation='ת"ת'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק ביצוע תביעה בהוצאה לפועל", abbreviation='ת"ת')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק", abbreviation="ת'"))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק אזרחי בסדר דין מיוחד", abbreviation='תא"ח')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק אזרחי בסדר דין מהיר", abbreviation='תא"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק אפוטרופסות", abbreviation='תא"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק אזרחי בסדר דין מקוצר", abbreviation='תא"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תובענה ארגונית בין עובד לארגון עובדים", abbreviation='תא"ר')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק אזרחי דיון מהיר", abbreviation='תאד"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בחירות כלליות", abbreviation='תב"כ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בחירות לכנסת", abbreviation='תב"כ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בחירות מיוחדות", abbreviation='תב"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בית דין אזורי לעבודה", abbreviation='תב"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעה לפי חוק ביטוח בריאות ממלכתי", abbreviation='תב"ר')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעת גברא", abbreviation='תג"א'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק תאונת דרכים אדום", abbreviation='תד"א')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק הסגרה", abbreviation='תה"ג'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק התרת נישואין", abbreviation='תה"ן')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק הסכם", abbreviation='תה"ס'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק הוצאה לפועל", abbreviation='תהוצל"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תכנון ובנייה – ועדות מקומיות", abbreviation='תו"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תכנון ובנייה – ועדות מחוזיות", abbreviation='תו"ח')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק זמני", abbreviation='תז"ם'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title='תיק לפי חוק הפיקוח על מצרכים ושירותים, התשי"ח–1957', abbreviation='תח"פ'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="תיק תעבורה שהוגש בידי משרד התחבורה – מחלקת התביעות", abbreviation='תח"ת'
    )
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק אזרחי", abbreviation='תי"א'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק פלילי", abbreviation='תי"פ'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק לאיתור", abbreviation='תל"א'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title='תיק לאיתור – בג"ץ', abbreviation='תל"ב')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק לאיתור – פלילי", abbreviation='תל"פ')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעה לאחר הסדר התדיינויות במשפחה", abbreviation='תלה"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעה ממוכנת בסדר דין מקוצר", abbreviation='תמ"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תביעה ממוכנת בסדר דין רגיל", abbreviation='תמ"ר')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק משפחה", abbreviation='תמ"ש'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="מינוי תומך החלטות", abbreviation='תמה"ח')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעה נגזרת", abbreviation='תנ"ג'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תביעת נזקקות", abbreviation='תנ"ז'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תובענה ארגונית (בין עובד לארגון עובדים)", abbreviation='תע"א')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק פלילי בנייה", abbreviation='תפ"ב')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק פשע חמור", abbreviation='תפ"ח'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(
        title="תביעה לפינוי מושכר שאינו לפי חוק הגנת הדייר", abbreviation='תפ"ם'
    )
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק פלילי עדות קטין נפגע עבירה", abbreviation='תפ"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק פלילי קהילתי", abbreviation='תפ"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק פלילי פשע חמור עדות קטין נפגע עבירה", abbreviation='תפח"ע')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק קנס מיוחד", abbreviation='תק"ם')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק בחירות לרשויות מקומיות", abbreviation='תר"ם')
)
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק תחבורה", abbreviation='תת"ח'))
CASE_TYPES_ABBREVIATIONS.append(Abbreviation(title="תיק תעבורה", abbreviation='תת"ע'))
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק תעבורה קהילתי", abbreviation='תת"ק')
)
CASE_TYPES_ABBREVIATIONS.append(
    Abbreviation(title="תיק תעבורה אדום", abbreviation='תתע"א')
)
