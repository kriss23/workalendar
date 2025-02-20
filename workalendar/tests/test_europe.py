# coding=utf-8
from datetime import date
from workalendar.tests import GenericCalendarTest
from workalendar.europe import CzechRepublic
from workalendar.europe import Slovakia
from workalendar.europe import Finland
from workalendar.europe import Sweden
from workalendar.europe import France, FranceAlsaceMoselle
from workalendar.europe import Greece
from workalendar.europe import Hungary
from workalendar.europe import Iceland
from workalendar.europe import Italy
from workalendar.europe import Luxembourg
from workalendar.europe import Netherlands
from workalendar.europe import Norway
from workalendar.europe import Poland
from workalendar.europe import Portugal
from workalendar.europe import Spain
from workalendar.europe import UnitedKingdom
from workalendar.europe import UnitedKingdomNorthernIreland
from workalendar.europe import EuropeanCentralBank
from workalendar.europe import Belgium
from workalendar.europe import (Germany, BadenWurttemberg, Bavaria, Berlin,
                                Brandenburg, Bremen, Hamburg, Hesse,
                                MecklenburgVorpommern, LowerSaxony,
                                NorthRhineWestphalia, RhinelandPalatinate,
                                Saarland, Saxony, SaxonyAnhalt,
                                SchleswigHolstein, Thuringia)


class CzechRepublicTest(GenericCalendarTest):
    cal_class = CzechRepublic

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 7, 6), holidays)
        self.assertIn(date(2013, 9, 28), holidays)
        self.assertIn(date(2013, 10, 28), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)


class SlovakiaTest(GenericCalendarTest):
    cal_class = Slovakia

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 1, 6), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 8), holidays)
        self.assertIn(date(2013, 7, 5), holidays)
        self.assertIn(date(2013, 8, 29), holidays)
        self.assertIn(date(2013, 9, 1), holidays)
        self.assertIn(date(2013, 9, 15), holidays)
        self.assertIn(date(2013, 11, 1), holidays)
        self.assertIn(date(2013, 11, 17), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)


class SwedenTest(GenericCalendarTest):
    cal_class = Sweden

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 6), holidays)  # national day
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints
        self.assertIn(date(2013, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2013, 12, 25), holidays)  # xmas day
        self.assertIn(date(2013, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2013, 12, 31), holidays)  # new year's eve

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # new year
        self.assertIn(date(2014, 1, 6), holidays)  # epiphany
        self.assertIn(date(2014, 4, 18), holidays)  # good friday
        self.assertIn(date(2014, 4, 20), holidays)  # easter sunday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # may day
        self.assertIn(date(2014, 5, 29), holidays)  # ascension
        self.assertIn(date(2014, 6, 6), holidays)  # national day
        self.assertIn(date(2014, 6, 8), holidays)  # pentecost
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints
        self.assertIn(date(2014, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2014, 12, 25), holidays)  # xmas day
        self.assertIn(date(2014, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2014, 12, 31), holidays)  # new year's eve

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # new year
        self.assertIn(date(2015, 1, 6), holidays)  # epiphany
        self.assertIn(date(2015, 4, 3), holidays)  # good friday
        self.assertIn(date(2015, 4, 5), holidays)  # easter sunday
        self.assertIn(date(2015, 4, 6), holidays)  # easter monday
        self.assertIn(date(2015, 5, 1), holidays)  # may day
        self.assertIn(date(2015, 5, 14), holidays)  # ascension
        self.assertIn(date(2015, 5, 24), holidays)  # pentecost
        self.assertIn(date(2015, 6, 6), holidays)  # national day
        self.assertIn(date(2015, 6, 19), holidays)  # midsummer eve
        self.assertIn(date(2015, 6, 20), holidays)  # midsummer day
        self.assertIn(date(2015, 10, 31), holidays)  # all saints
        self.assertIn(date(2015, 12, 24), holidays)  # xmas eve
        self.assertIn(date(2015, 12, 25), holidays)  # xmas day
        self.assertIn(date(2015, 12, 26), holidays)  # second day of xmas
        self.assertIn(date(2015, 12, 31), holidays)  # new year's eve


class FinlandTest(GenericCalendarTest):
    cal_class = Finland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # may day
        self.assertIn(date(2013, 5, 9), holidays)  # ascension
        self.assertIn(date(2013, 5, 19), holidays)  # pentecost
        self.assertIn(date(2013, 6, 21), holidays)  # midsummer eve
        self.assertIn(date(2013, 6, 22), holidays)  # midsummer day
        self.assertIn(date(2013, 11, 2), holidays)  # all saints (special)
        self.assertIn(date(2013, 12, 6), holidays)  # Independence day
        self.assertIn(date(2013, 12, 24), holidays)  # XMas eve
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens

    def test_year_2014(self):
        # testing the special rule variable holidays
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 20), holidays)  # midsummer eve
        self.assertIn(date(2014, 6, 21), holidays)  # midsummer day
        self.assertIn(date(2014, 11, 1), holidays)  # all saints (special)


class FranceTest(GenericCalendarTest):

    cal_class = France

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 4, 1), holidays)   # easter
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 8), holidays)   # 39-45
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 20), holidays)  # Pentecote
        self.assertIn(date(2013, 7, 14), holidays)  # Nation day
        self.assertIn(date(2013, 8, 15), holidays)  # Assomption
        self.assertIn(date(2013, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2013, 11, 11), holidays)  # Armistice
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas

    def test_working_days(self):
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 1)))  # holiday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 5)))  # saturday
        self.assertFalse(self.cal.is_working_day(date(2013, 1, 6)))  # sunday
        self.assertTrue(self.cal.is_working_day(date(2013, 1, 7)))   # monday

    def test_business_days_computations(self):
        day = date(2013, 10, 30)
        self.assertEquals(
            self.cal.add_working_days(day, 0), date(2013, 10, 30))
        self.assertEquals(
            self.cal.add_working_days(day, 1), date(2013, 10, 31))
        self.assertEquals(self.cal.add_working_days(day, 2), date(2013, 11, 4))
        self.assertEquals(self.cal.add_working_days(day, 3), date(2013, 11, 5))


class FranceAlsaceMoselleTest(FranceTest):
    cal_class = FranceAlsaceMoselle

    def test_year_2013(self):
        super(FranceAlsaceMoselleTest, self).test_year_2013()
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 29), holidays)  # Good friday
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing day

    def test_working_days(self):
        super(FranceAlsaceMoselleTest, self).test_working_days()

    def test_business_days_computations(self):
        super(FranceAlsaceMoselleTest, self) \
            .test_business_days_computations()


class GreeceTest(GenericCalendarTest):
    cal_class = Greece

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year
        self.assertIn(date(2013, 1, 6), holidays)  # epiphany
        self.assertIn(date(2013, 3, 18), holidays)  # Clean monday
        # Annunciation & Independence day
        self.assertIn(date(2013, 3, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)  # labour day
        self.assertIn(date(2013, 5, 3), holidays)  # good friday
        self.assertIn(date(2013, 5, 5), holidays)  # easter
        self.assertIn(date(2013, 5, 6), holidays)  # easter monday
        self.assertIn(date(2013, 6, 23), holidays)  # pentecost sunday
        self.assertIn(date(2013, 6, 24), holidays)  # whit monday
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 10, 28), holidays)  # Ochi Day
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Glorifying mother of God


class HungaryTest(GenericCalendarTest):
    cal_class = Hungary

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 15), holidays)  # national day
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labour day
        self.assertIn(date(2013, 5, 19), holidays)  # Whit sunday
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 8, 20), holidays)  # St Stephen's day
        self.assertIn(date(2013, 10, 23), holidays)  # national day (again?)
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 25), holidays)  # XMas
        self.assertIn(date(2013, 12, 26), holidays)  # Second day of XMas


class NorwayTest(GenericCalendarTest):
    cal_class = Norway

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)   # new year
        self.assertIn(date(2013, 3, 28), holidays)   # maundy thursday
        self.assertIn(date(2013, 3, 29), holidays)   # good friday
        self.assertIn(date(2013, 3, 31), holidays)   # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)   # easter monday
        self.assertIn(date(2013, 5, 1), holidays)   # labour day
        self.assertIn(date(2013, 5, 17), holidays)   # constitution day
        self.assertIn(date(2013, 5, 9), holidays)   # Ascension
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 20), holidays)  # Whit monday
        self.assertIn(date(2013, 12, 25), holidays)  # Xmas
        self.assertIn(date(2013, 12, 26), holidays)  # St Stephens


class PolandTest(GenericCalendarTest):
    cal_class = Poland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # New Year
        self.assertIn(date(2013, 1, 6), holidays)  # Trzech Kroli
        self.assertIn(date(2013, 3, 31), holidays)  # Easter Sunday
        self.assertIn(date(2013, 4, 1), holidays)  # Easter Monday
        self.assertIn(date(2013, 5, 1), holidays)  # Labor Day
        self.assertIn(date(2013, 5, 3), holidays)  # Constitution Day
        self.assertIn(date(2013, 5, 19), holidays)  # Pentecost
        self.assertIn(date(2013, 5, 30), holidays)  # Corpus Christi
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # All Saints' Day
        self.assertIn(date(2013, 11, 11), holidays)  # Independence Day
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas Day
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day


class IcelandTest(GenericCalendarTest):
    cal_class = Iceland

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)
        self.assertIn(date(2013, 3, 28), holidays)
        self.assertIn(date(2013, 3, 29), holidays)
        self.assertIn(date(2013, 4, 1), holidays)
        self.assertIn(date(2013, 4, 25), holidays)
        self.assertIn(date(2013, 5, 1), holidays)
        self.assertIn(date(2013, 5, 9), holidays)
        self.assertIn(date(2013, 5, 20), holidays)
        self.assertIn(date(2013, 6, 17), holidays)
        self.assertIn(date(2013, 8, 5), holidays)
        self.assertIn(date(2013, 12, 24), holidays)
        self.assertIn(date(2013, 12, 25), holidays)
        self.assertIn(date(2013, 12, 26), holidays)
        self.assertIn(date(2013, 12, 31), holidays)


class ItalyTest(GenericCalendarTest):
    cal_class = Italy

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new years day
        self.assertIn(date(2013, 1, 6), holidays)  # Epiphany
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 4, 25), holidays)  # liberation day
        self.assertIn(date(2013, 5, 1), holidays)  # workers day
        self.assertIn(date(2013, 6, 2), holidays)  # Republic day
        self.assertIn(date(2013, 8, 15), holidays)  # Assumption
        self.assertIn(date(2013, 11, 1), holidays)  # all saints
        self.assertIn(date(2013, 12, 8), holidays)  # immaculate Conception
        self.assertIn(date(2013, 12, 25), holidays)  # christmas
        self.assertIn(date(2013, 12, 26), holidays)  # San Stefano


class LuxembourgTest(GenericCalendarTest):

    cal_class = Luxembourg

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)   # new year
        self.assertIn(date(2016, 3, 28), holidays)   # easter
        self.assertIn(date(2016, 5, 1), holidays)   # labour day
        self.assertIn(date(2016, 5, 5), holidays)   # Ascension
        self.assertIn(date(2016, 5, 16), holidays)  # Pentecote
        self.assertIn(date(2016, 6, 23), holidays)  # Luxembourg National Day
        self.assertIn(date(2016, 8, 15), holidays)  # Assomption
        self.assertIn(date(2016, 11, 1), holidays)  # Toussaint
        self.assertIn(date(2016, 12, 25), holidays)  # Christmas
        self.assertIn(date(2016, 12, 26), holidays)  # St. Stephen´s Day


class NetherlandsTest(GenericCalendarTest):

    cal_class = Netherlands

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)   # New Year
        self.assertIn(date(2015, 4, 3), holidays)   # Good friday
        self.assertIn(date(2015, 4, 5), holidays)   # Easter Sunday
        self.assertIn(date(2015, 4, 6), holidays)   # Easter Monday
        self.assertIn(date(2015, 4, 27), holidays)  # King's Day
        self.assertIn(date(2015, 5, 5), holidays)   # Liberation Day
        self.assertIn(date(2015, 5, 14), holidays)  # Ascension
        self.assertIn(date(2015, 5, 24), holidays)  # whit sunday
        self.assertIn(date(2015, 5, 25), holidays)  # whit monday
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas
        self.assertIn(date(2015, 12, 26), holidays)  # St. Stephen´s Day

    def test_year_2025(self):
        """ In 2025 King's Day is on 26 April """
        holidays = self.cal.holidays_set(2025)
        self.assertIn(date(2025, 4, 26), holidays)   # King's Day


class UnitedKingdomTest(GenericCalendarTest):
    cal_class = UnitedKingdom

    def test_year_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 1, 1), holidays)  # new year day
        self.assertIn(date(2013, 3, 29), holidays)  # good friday
        self.assertIn(date(2013, 3, 31), holidays)  # easter sunday
        self.assertIn(date(2013, 4, 1), holidays)  # easter monday
        self.assertIn(date(2013, 5, 6), holidays)  # Early May Bank Holiday
        self.assertIn(date(2013, 5, 27), holidays)  # Spring Bank Holiday
        self.assertIn(date(2013, 8, 26), holidays)  # Late Summer Bank Holiday
        self.assertIn(date(2013, 12, 25), holidays)  # Christmas
        self.assertIn(date(2013, 12, 26), holidays)  # Boxing Day

    def test_shift_2012(self):
        holidays = self.cal.holidays_set(2012)
        self.assertIn(date(2012, 1, 1), holidays)  # new year day
        self.assertIn(date(2012, 1, 2), holidays)  # new year day shift

    def test_shift_2011(self):
        holidays = self.cal.holidays_set(2011)
        self.assertIn(date(2011, 12, 25), holidays)  # Christmas it's sunday
        self.assertIn(date(2011, 12, 26), holidays)  # XMas day shift
        self.assertIn(date(2011, 12, 27), holidays)  # Boxing day shift

    def test_shift_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 12, 25), holidays)  # Christmas it's friday
        self.assertIn(date(2015, 12, 26), holidays)  # Boxing day it's saturday
        self.assertIn(date(2015, 12, 28), holidays)  # Boxing day shift


class UnitedKingdomNorthernIrelandTest(UnitedKingdomTest):
    cal_class = UnitedKingdomNorthernIreland

    def test_regional_2013(self):
        holidays = self.cal.holidays_set(2013)
        self.assertIn(date(2013, 3, 17), holidays)  # St Patrick's day
        self.assertIn(date(2013, 3, 18), holidays)  # St Patrick's sub
        self.assertIn(date(2013, 7, 12), holidays)  # Battle of the Boyne

    def test_regional_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 7, 12), holidays)  # Battle of the Boyne
        self.assertIn(date(2014, 7, 14), holidays)  # Battle of the Boyne sub


class EuropeanCentralBankTest(GenericCalendarTest):
    cal_class = EuropeanCentralBank

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)  # New year's day
        self.assertIn(date(2014, 4, 18), holidays)  # Good friday
        self.assertIn(date(2014, 4, 21), holidays)  # easter monday
        self.assertIn(date(2014, 5, 1), holidays)  # Labour day
        self.assertIn(date(2014, 12, 25), holidays)  # XMas
        self.assertIn(date(2014, 12, 26), holidays)  # St Stephen


class BelgiumTest(GenericCalendarTest):
    cal_class = Belgium

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 7, 21), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 11, 1), holidays)
        self.assertIn(date(2014, 11, 11), holidays)
        self.assertIn(date(2014, 12, 25), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 7, 21), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)


class GermanyTest(GenericCalendarTest):
    cal_class = Germany

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class BadenWurttembergTest(GermanyTest):
    cal_class = BadenWurttemberg

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 6), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class BavariaTest(GenericCalendarTest):
    cal_class = Bavaria

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 1, 6), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 11, 1), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 11, 1), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class BerlinTest(GermanyTest):
    cal_class = Berlin


class BrandenburgTest(GenericCalendarTest):
    cal_class = Brandenburg

    def test_year_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 1, 1), holidays)
        self.assertIn(date(2014, 4, 18), holidays)
        self.assertIn(date(2014, 4, 21), holidays)
        self.assertIn(date(2014, 5, 1), holidays)
        self.assertIn(date(2014, 5, 29), holidays)
        self.assertIn(date(2014, 6, 9), holidays)
        self.assertIn(date(2014, 10, 3), holidays)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 12, 25), holidays)
        self.assertIn(date(2014, 12, 26), holidays)

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 4, 6), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 5, 14), holidays)
        self.assertIn(date(2015, 5, 25), holidays)
        self.assertIn(date(2015, 10, 3), holidays)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
        self.assertIn(date(2015, 12, 26), holidays)


class BremenTest(GermanyTest):
    cal_class = Bremen


class HamburgTest(GermanyTest):
    cal_class = Hamburg


class HesseTest(GermanyTest):
    cal_class = Hesse

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)


class MecklenburgVorpommernTest(GermanyTest):
    cal_class = MecklenburgVorpommern

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)


class LowerSaxonyTest(GermanyTest):
    cal_class = LowerSaxony


class NorthRhineWestphaliaTest(GermanyTest):
    cal_class = NorthRhineWestphalia

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class RhinelandPalatinateTest(GermanyTest):
    cal_class = RhinelandPalatinate

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class SaarlandTest(GermanyTest):
    cal_class = Saarland

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 6, 19), holidays)
        self.assertIn(date(2014, 8, 15), holidays)
        self.assertIn(date(2014, 11, 1), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 6, 4), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 11, 1), holidays)


class SaxonyTest(GermanyTest):
    cal_class = Saxony

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 11, 19), holidays)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 11, 18), holidays)
        self.assertIn(date(2015, 10, 31), holidays)


class SaxonyAnhaltTest(GermanyTest):
    cal_class = SaxonyAnhalt

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)
        self.assertIn(date(2014, 1, 6), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)
        self.assertIn(date(2015, 1, 6), holidays)


class SchleswigHolsteinTest(GermanyTest):
    cal_class = SchleswigHolstein


class ThuringiaTest(GermanyTest):
    cal_class = Thuringia

    def test_extra_2014(self):
        holidays = self.cal.holidays_set(2014)
        self.assertIn(date(2014, 10, 31), holidays)

    def test_extra_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 10, 31), holidays)


class PortugalTest(GenericCalendarTest):
    cal_class = Portugal

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2015, 2, 17), holidays)  # Entrudo
        self.assertIn(date(2015, 4, 3), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2015, 4, 5), holidays)  # Domingo de Páscoa
        self.assertIn(date(2015, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2015, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2015, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2015, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2015, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2015, 12, 25), holidays)  # Natal

    def test_year_2016(self):
        holidays = self.cal.holidays_set(2016)
        self.assertIn(date(2016, 1, 1), holidays)  # Ano Novo
        self.assertIn(date(2016, 2, 9), holidays)  # Entrudo
        self.assertIn(date(2016, 3, 25), holidays)  # Sexta-Feira Santa
        self.assertIn(date(2016, 3, 27), holidays)  # Domingo de Páscoa
        self.assertIn(date(2016, 4, 25), holidays)  # Dia da Liberdade
        self.assertIn(date(2016, 5, 1), holidays)  # Dia do Trabalhador
        self.assertIn(date(2016, 6, 10), holidays)  # Dia de Portugal
        self.assertIn(date(2016, 8, 15), holidays)  # Assunção de Nossa Senhora
        self.assertIn(date(2016, 12, 8), holidays)  # Imaculada Conceição
        self.assertIn(date(2016, 12, 25), holidays)  # Natal


class Spain(GenericCalendarTest):
    cal_class = Spain

    def test_year_2015(self):
        holidays = self.cal.holidays_set(2015)
        self.assertIn(date(2015, 1, 1), holidays)
        self.assertIn(date(2015, 1, 6), holidays)
        self.assertIn(date(2015, 4, 3), holidays)
        self.assertIn(date(2015, 5, 1), holidays)
        self.assertIn(date(2015, 8, 15), holidays)
        self.assertIn(date(2015, 10, 12), holidays)
        self.assertIn(date(2015, 12, 8), holidays)
        self.assertIn(date(2015, 12, 25), holidays)
