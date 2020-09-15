from datetime import date
import datetime
from matplotlib import pyplot as plt
import numpy as np
import calendar
import pandas

jan_holidays={ "01-01-2020":"New Year's day",
                       "02-01-2020":"Guru Govind Singh Jayanthi",
                       "14-01-2020":"Lohri",
                       "15-01-2020":"Pongal",
                       "15-01-2020":"Makar sankranthi",
                       "25-01-2020":"Chinese new year",
                       "26-01-2020":"Republic day",
                       "30-01-2020":"Vasant Panchami"
                       }
feb_holidays={
                       "09-02-2020":"Guru Ravidas jayanthi",
                       "14-02-2020":"Valentine's day",
                       "18-02-2020":"Maharshi Dayanand Saraswati Jayanti",
                       "19-02-2020":"Shivaji Jayanti",
                       "21-02-2020":"Maha Shiva ratri"
        }
march_holidays={
                        "21-03-2020":"Maha Shivaratri",
                        "09-03-2020":"Holika Dahana",
            "10-03-2020":"Holi",
            "20-03-2020":"March Equinox","25-03-2020":"Chaitra Sukhladi"
        }
april_holidays={
            "06-04-2020":"Mahavir Jayanti","09-04-2020":"First day of Passover","10-04-2020":"Good Friday","12-04-2020":"Easter Day","13-04-2020":"Vaisakhi",
             "14-04-2020":"Mesadi","14-04-2020":"Ambedkar Jayanti"       }
may_holidays={
            "01-05-2020":"May day","07-05-2020":"Budhha Purnami","07-05-2020":"Birthday of Rabindranath","10-05-2020":"Mother's day","22-05-2020":"Jamat UI-Vida",
            "25-05-2020":"Ramzan id/Eid-ul-Fitar",
        }
jun_holidays={
            "21-06-2020":"June Solstice","21-06-2020":"Father's Day","23-06-2020":"Rath Yatra","05-06-2020":"Guru Purnima"
        }
aug_holidays={
            "01-08-2020":"Bakr id/Eid ul-Adha","01-08-2020":"Friendship Day","03-08-2020":"Raksha Bandhan(Rakhi)",
            "11-08-2020":"Janmashtami(Smarta)","12-08-2020":"Jannmashtami","15-08-2020":"Independence Day","16-08-2020":"Parsi New Year"
            ,"22-08-2020":"Ganesh Chaturthi/Vinayak Chavithi","30-08-2020":"Muharram/Ashura","31-08-2020":"Onam"
        }
sep_holidays={
            "22-09-2020":"September Equinox"
        }
oct_holidays={
            "02-10-2020":"Mahatma Gandhi Jayanti","22-10-2020":"Maha Saptami","23-10-2020":"Maha Ashtami","24-10-2020":"Maha Navami"
            ,"25-10-2020":"Dussehra","29-10-2020":"Milad un-Nabi/Id-e-Milad","31-10-2020":"Halloween","31-10-2020":"Maha rishi valmiki Jayanthi"
        }
nov_holidays={
            "04-11-2020":"Karaka Chaturthi(Karva Chauth)","14-11-2020":"Naraka Chaturdasi","14-11-2020":"Divali","15-11-2020":"Govardhan Puja",
            "16-11-2020":"Bhai Duj","20-11-2020":"Chat Puja","24-11-2020":"Guru Tegh Baahadur's Martyrdom Day","30-11-2020":"Guru Nanak Jayanthi"
        }
dec_holidays={
            "11-12-2020":"First day of Hanukkah","18-12-2020":"Last day of Hanukkah","21-12-2020":"December Solstice","24-12-2020":"Christmas Eve",
            "25-12-2020":"Christmas","31-12-2020":"New Year's Eve"
        }

total_holidays={1:jan_holidays,2:feb_holidays,3:march_holidays,4:april_holidays,5:may_holidays,6:jun_holidays,8:aug_holidays,9:sep_holidays,
                10:oct_holidays,11:nov_holidays,12:dec_holidays}


def month(month):
        if month=='January':
            print(pandas.Series(jan_holidays))
            cal=input("do you want to see the calendar?")
            if cal.lower()=='yes':
                print(calendar.month(2020,1))
        elif month=='February':
            for i in feb_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,2))
        elif month=='March':
            for i in march_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,3))
        elif month=='April':
            for i in april_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,4))
        elif month=='May':
            for i in may_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                 print(calendar.month(2020,5))
        elif month=='June':
            for i in jun_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,6))
        elif month=='August':
            for i in aug_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,8))
        elif month=='September':
            for i in sep_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,9))
        elif month=='October':
            for i in oct_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,10))
        elif month=='November':
            for i in nov_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,11))
        elif month=='December':
            for i in dec_holidays.items():
                print(i)
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,12))
        elif month=='July':
            print("***there are no holidays this month...***")
            cal = input("do you want to see the calendar?")
            if cal.lower() == 'yes':
                print(calendar.month(2020,7))


def day(day):
    for i in total_holidays.values():
        for j in i.keys():
            if day==j:
                print(i[j])

doubt=input("do you wanna search by festival name?")
if doubt=='yes':
    festival=input("enter the festival name")
    for i in total_holidays.values():
        for key,values in i.items():
            if festival in values:
                print(key)











