#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/client/base.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import re

from dataclasses import dataclass
from typing import Self

from ..models import Abbreviation, CourtAbbreviation, DecisionsCollection
from ..helpers import intervals_to_str, get_obj_from_abbreviation
from ..assets import (
    CASE_TYPES_ABBREVIATIONS,
    COURT_ABBREVIATIONS,
    COURT_SEATS,
    DECISIONS_COLLECTIONS,
    LEGISLATION_COLLECTIONS,
)

__all__ = [
    "IsraeliLegislation",
    "IsraeliDecision",
]


@dataclass
class IsraeliLegislation:
    specific_reference: int | str | list[int | str] | None = None
    legislation_title: str | None = None
    legislation_hebrew_year: str | None = None
    legislation_year: str | None = None
    legislation_collection: Abbreviation | str | None = None
    legislation_collection_year: str | None = None
    first_page_index: int | None = None
    specific_page_index_reference: int | list[int] | None = None

    @property
    def _legislation_collection(self) -> Abbreviation | None:
        if isinstance(self.legislation_collection, str):
            obj: Abbreviation = get_obj_from_abbreviation(
                self.legislation_collection, LEGISLATION_COLLECTIONS
            )
            if obj:
                return obj
            else:
                return None
        else:
            return self.legislation_collection

    @property
    def _specific_page_index_reference(self) -> str:
        if isinstance(self.specific_page_index_reference, list):
            return intervals_to_str(self.specific_page_index_reference)
        else:
            return str(self.specific_page_index_reference)

    def from_str(s: str) -> Self | None:
        ptn = re.compile(
            r"^(.+? ל)?(.+?), (התש\w?\"\w–\d{4})?,? ?(.+?)? ?(התש\w?\"\w)? ?(\d{1,})?,? ?(\d{1,})?$"
        )
        m = re.match(ptn, s)
        if m:
            if m.group(1):
                _section = m.group(1).strip().removesuffix("ל").strip()
            else:
                _section = None
            if m.group(2):
                _legislation_title = (
                    m.group(2).strip().removesuffix(",").strip().removesuffix(",")
                )
            else:
                _legislation_title = None
            if m.group(3):
                _legislation_years = m.group(3).strip().removesuffix(",").split("–", 1)
                _legislation_hebrew_year = _legislation_years[0].strip()
                _legislation_year = _legislation_years[1].strip()
            else:
                _legislation_hebrew_year = None
                _legislation_year = None
            if m.group(4):
                _legislation_collection = m.group(4).strip().removesuffix(",").strip()
            else:
                _legislation_collection = None
            if m.group(5):
                _legislation_collection_year = (
                    m.group(5).strip().removesuffix(",").strip()
                )
            else:
                _legislation_collection_year = None
            if m.group(6) and m.group(7):
                _first_page_index = m.group(6).strip().removesuffix(",").strip()
                _specific_page_index_reference = (
                    m.group(7).strip().removesuffix(",").strip()
                )
            elif m.group(7):
                _first_page_index = m.group(7).strip().removesuffix(",").strip()
                _specific_page_index_reference = None
            elif m.group(6):
                _first_page_index = m.group(6).strip().removesuffix(",").strip()
                _specific_page_index_reference = None
            else:
                _first_page_index = None
                _specific_page_index_reference = None
            return IsraeliLegislation(
                specific_reference=_section,
                legislation_title=_legislation_title,
                legislation_hebrew_year=_legislation_hebrew_year,
                legislation_year=_legislation_year,
                legislation_collection=_legislation_collection,
                legislation_collection_year=_legislation_collection_year,
                first_page_index=_first_page_index,
                specific_page_index_reference=_specific_page_index_reference,
            )
        else:
            return None

    def __str__(self) -> str:
        s = ""
        if self.specific_reference:
            s += f"{self.specific_reference} ל"
        if self.legislation_title:
            s += f"{self.legislation_title}"
        if self.legislation_hebrew_year:
            s += f", {self.legislation_hebrew_year}"
        if self.legislation_year:
            s += f"–{self.legislation_year}"
        if self.legislation_collection:
            if self._legislation_collection:
                s += f", {self._legislation_collection.abbreviation}"
            else:
                s += f", {self.legislation_collection}"
        if self.legislation_collection_year:
            s += f" {self.legislation_collection_year}"
        if self.first_page_index:
            s += f" {self.first_page_index}"
        if self.specific_page_index_reference:
            s += f", {self._specific_page_index_reference}"
        return s


@dataclass
class IsraeliDecision:
    proceeding_type: Abbreviation | str | None = None
    court_type: CourtAbbreviation | str | None = None
    court_seat: Abbreviation | str | None = None
    docket_id: str | None = None
    principle_proceeding_type: Abbreviation | str | None = None
    principle_docket_id: str | None = None
    plaintiff: str | None = None
    respondent: str | None = None
    publication: DecisionsCollection | str | None = None
    volume: int | str | None = None
    edition: int | str | None = None
    first_page_index: int | str | None = None
    specific_reference: int | list[int] | str | None = None
    decision_year: int | str | None = None

    @property
    def _proceeding_type(self) -> Abbreviation | None:
        if isinstance(self.proceeding_type, str):
            obj: Abbreviation = get_obj_from_abbreviation(
                self.proceeding_type, CASE_TYPES_ABBREVIATIONS
            )
            if obj:
                return obj
            else:
                return None
        else:
            return self.proceeding_type

    @property
    def _court_type(self) -> CourtAbbreviation | None:
        if isinstance(self.court_type, str):
            obj: CourtAbbreviation = get_obj_from_abbreviation(
                self.court_type,
                COURT_ABBREVIATIONS,
                (self.proceeding_type, self.publication, self.decision_year),
            )
            if obj:
                return obj
            else:
                return None
        else:
            return self.court_type

    @property
    def _court_seat(self) -> Abbreviation | None:
        if isinstance(self.court_seat, str):
            obj: Abbreviation = get_obj_from_abbreviation(self.court_seat, COURT_SEATS)
            if obj:
                return obj
            else:
                return None
        else:
            return self.court_seat

    @property
    def _principle_proceeding_type(self) -> Abbreviation | None:
        if isinstance(self.principle_proceeding_type, str):
            obj: Abbreviation = get_obj_from_abbreviation(
                self.principle_proceeding_type, CASE_TYPES_ABBREVIATIONS
            )
            if obj:
                return obj
            else:
                return None
        else:
            return self.principle_proceeding_type

    @property
    def _publication(self) -> DecisionsCollection | None:
        if isinstance(self.publication, str):
            obj: DecisionsCollection = get_obj_from_abbreviation(
                self.publication, DECISIONS_COLLECTIONS
            )
            if obj:
                return obj
            else:
                return None
        else:
            return self.publication

    @property
    def _specific_reference(self) -> str:
        if isinstance(self.specific_reference, list):
            return intervals_to_str(self.specific_reference)
        else:
            return str(self.specific_reference)

    def from_str(s: str) -> Self | None:
        ptn = re.compile(
            r"^(.*?) (\(.*?\) )?(.*?) (?:\[bold\])?(.*?) (?:נ'|–) (.*?)(?:\[\/bold\])?, ([^\(]+) ([^\(]+)(\(.*?\))?(.*?)(, .*?)? \((.*?)\)$"
        )
        m = re.match(ptn, s)
        if m:
            if m.group(1):
                _proceeding_type = m.group(1).strip()
            else:
                _proceeding_type = None
            if m.group(2):
                _court_type_and_seat = (
                    m.group(2).strip().removeprefix("(").removesuffix(")").split(" ", 1)
                )
                _court_type = _court_type_and_seat[0].strip()
                _court_seat = _court_type_and_seat[1].strip()
            else:
                _court_type, _court_seat = None, None
            if m.group(3):
                _docket_id = m.group(3).strip()
            else:
                _docket_id = None
            if m.group(4):
                _plaintiff = m.group(4).strip()
            else:
                _plaintiff = None
            if m.group(5):
                _respondent = m.group(5).strip()
            else:
                _respondent = None
            if m.group(6):
                _publication = m.group(6).strip()
            else:
                _publication = None
            if m.group(7):
                _volume = m.group(7).strip()
            else:
                _volume = None
            if m.group(8):
                _edition = (
                    m.group(8).strip().removeprefix("(").removesuffix(")").strip()
                )
            else:
                _edition = None
            if m.group(9):
                _first_page_index = m.group(9).strip()
            else:
                _first_page_index = None
            if m.group(10):
                _specific_reference = m.group(10).strip().removeprefix(",").strip()
            else:
                _specific_reference = None
            if m.group(11):
                _decision_year = m.group(11).strip()
            else:
                _decision_year = None

            print(
                f"{_proceeding_type=}\n{_court_type=}\n{_court_seat=}\n{_docket_id=}\n{_plaintiff=}\n{_respondent=}\n{_publication=}\n{_volume=}\n{_edition}\n{_first_page_index=}\n{_specific_reference}\n{_decision_year=}"
            )
            return IsraeliDecision(
                proceeding_type=_proceeding_type,
                court_type=_court_type,
                court_seat=_court_seat,
                docket_id=_docket_id,
                plaintiff=_plaintiff,
                respondent=_respondent,
                publication=_publication,
                volume=_volume,
                edition=_edition,
                first_page_index=_first_page_index,
                specific_reference=_specific_reference,
                decision_year=_decision_year,
            )
        else:
            return None

    def __str__(self) -> str:
        s = ""
        if self.proceeding_type:
            if self._proceeding_type:
                s += f"{self._proceeding_type.abbreviation}"
            else:
                s += f"{self.proceeding_type}"
        if self.court_type:
            if self._court_type:
                s += f" ({self._court_type.abbreviation}"
            else:
                s += f" ({self.court_type}"
        if self.court_seat:
            if self._court_seat:
                s += f" {self._court_seat.abbreviation})"
            else:
                s += f" {self.court_seat})"
        if self.docket_id:
            s += f" {self.docket_id}"
        if self.principle_proceeding_type:
            if self._principle_proceeding_type:
                s += f" ({self._principle_proceeding_type.abbreviation}"
            else:
                s += f" ({self.principle_proceeding_type}"
        if self.principle_docket_id:
            s += f" {self.principle_docket_id})"
        if self.plaintiff:
            s += f" [bold]{self.plaintiff}"
        if self._court_type and self.respondent:
            s += f" {self._court_type.separator} {self.respondent}[/bold]"
        elif self.respondent:
            s += f" נ' {self.respondent}[/bold]"
        else:
            s += "[/bold]"
        if self.publication:
            if self._publication:
                s += f", {self._publication.abbreviation}"
            else:
                s += f", {self.publication}"
        if self.volume:
            s += f" {self.volume}"
        if self.edition:
            s += f"({self.edition})"
        # Rule 1.9
        if (
            self.volume
            and not self.edition
            and (isinstance(self.volume, int) or self.volume[-1].isdigit())
            and isinstance(self.first_page_index, int)
        ) or (
            self.volume
            and not self.edition
            and isinstance(self.volume, str)
            and self.volume[-1].isalpha()
            and isinstance(self.first_page_index, str)
            and self.first_page_index[0].isalpha()
        ):
            s += ","
        if self.first_page_index:
            s += f" {self.first_page_index}"
        if self.specific_reference:
            s += f", {self._specific_reference}"
        if self.decision_year:
            s += f" ({self.decision_year})"
        return s
