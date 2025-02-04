# Datetime Calculator by Avner

"""PYTHON بداية الدوال - الرجاء عدم الحذف - بواسطة Avner"""
import math
باي = math.pi
def اطبع(*args, **kwargs): print(*args, **kwargs)
def عدد(x): return int(x)
def عشري(x): return float(x)
def الطول(x): return len(x)
def ادخال(تلميح=""): return input(تلميح)
def نطاق(بداية, نهاية=None, خطوة=1): return list(range(بداية, نهاية, خطوة))
def المجموع(قائمة, start=0): return start + sum(قائمة)
def أي(قائمة): return any(قائمة)
def الكل(قائمة): return all(قائمة)
def ترتيب(قائمة, key=None, reverse=False): return sorted(قائمة, key=key, reverse=reverse)
def عكس(قائمة): return reversed(قائمة)
def ربط(*قوائم): return zip(*قوائم)
def ترقيم(تسلسل, البداية=0): return list(enumerate(تسلسل, start=البداية))
def مطلق(x): return abs(x)
def تقريب(رقم, ndigits=None): return round(رقم, ndigits)
def أدنى(*args): return min(args[0]) if len(args) == 1 and hasattr(args[0], '__iter__') else min(args)
def أعلى(*args): return max(args[0]) if len(args) == 1 and hasattr(args[0], '__iter__') else max(args)
def تنسيق(string, *args, **kwargs): return string.format(*args, **kwargs) if args or kwargs else string
def حرف(رقم): return chr(رقم)
def ترقيم_رمزي(حرف): return ord(حرف)
def أس(رقم, مؤشر): return رقم ** مؤشر
def تعيين(دالة, تكرار, *تكرارات_أخرى): 
    return list(map(دالة, تكرار)) if not تكررات_أخرى else [دالة(*items) for items in zip(تكرار, *تكررات_أخرى)]

def is_leap_year(السنة):
    return السنة % 4 == 0 and (السنة % 100 != 0 or السنة % 400 == 0)

def days_in_month(الشهر):
    قائمة_الأيام = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return قائمة_الأيام[الشهر]

def num_of_leap_years(سنة_البداية, سنة_النهاية):
    العداد = 0
    for السنة in range(سنة_البداية, سنة_النهاية):
        if is_leap_year(السنة):
            العداد += 1
    return العداد

def is_valid_date(التاريخ):
    if الطول(التاريخ) != 8:
        return False
    try:
        اليوم = int(التاريخ[:2])
        الشهر = int(التاريخ[2:4])
        السنة = int(التاريخ[4:])
    except ValueError:
        return False
    if الشهر < 1 or الشهر > 12:
        return False
    الأيام_القصوى = days_in_month(الشهر)
    if الشهر == 2 and is_leap_year(السنة):
        الأيام_القصوى = 29
    return 1 <= اليوم <= الأيام_القصوى

def num_of_days_from_1900(التاريخ):
    if not is_valid_date(التاريخ):
        return None
    اليوم = int(التاريخ[:2])
    الشهر = int(التاريخ[2:4])
    السنة = int(التاريخ[4:])
    عدد_الأيام = (السنة - 1900) * 365 + num_of_leap_years(1900, السنة)
    for شهر in range(1, الشهر):
        عدد_الأيام += days_in_month(shahr)
    if الشهر > 2 and is_leap_year(السنة):
        عدد_الأيام += 1
    عدد_الأيام += اليوم - 1
    return عدد_الأيام

def days_between_2_dates(التاريخ1, التاريخ2):
    عدد_الأيام1 = num_of_days_from_1900(التاريخ1)
    عدد_الأيام2 = num_of_days_from_1900(التاريخ2)
    if عدد_الأيام1 is None or عدد_الأيام2 is None:
        return None
    return مطلق(عدد_الأيام2 - عدد_الأيام1)

def add_n_days_after_1900(الأيام_المتبقية):
    السنة = 1900
    الشهر = 1
    اليوم = 1
    while الأيام_المتبقية >= 366 or (الأيام_المتبقية >= 365 and not is_leap_year(السنة)):
        if is_leap_year(السنة):
            if الأيام_المتبقية >= 366:
                الأيام_المتبقية -= 366
                السنة += 1
        else:
            الأيام_المتبقية -= 365
            السنة += 1
    while الأيام_المتبقية > 0:
        الأيام_القصوى = days_in_month(الشهر)
        if الشهر == 2 and is_leap_year(السنة):
            الأيام_القصوى = 29
        if الأيام_المتبقية >= الأيام_القصوى:
            الأيام_المتبقية -= الأيام_القصوى
            الشهر += 1
            if الشهر > 12:
                الشهر = 1
                السنة += 1
        else:
            اليوم += الأيام_المتبقية
            الأيام_المتبقية = 0
    return f"{اليوم:02d}{الشهر:02d}{السنة}"

def add_n_days_from_a_date(التاريخ, عدد_الأيام):
    if not is_valid_date(التاريخ):
        return None
    إجمالي_الأيام = num_of_days_from_1900(التاريخ) + عدد_الأيام
    return add_n_days_after_1900(إجمالي_الأيام)

def weekday_of_date(التاريخ):
    أيام_الأسبوع = ["الإثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد"]
    عدد_الأيام = num_of_days_from_1900(التاريخ)
    if عدد_الأيام is None:
        return None
    return أيام_الأسبوع[عدد_الأيام % 7]

def date_calculator():
    انتهى = False
    while not انتهى:
        اطبع("-----------------------------------------")
        اطبع("Welcome to date calculator")
        اطبع("  1. Calculate number of days between 2 dates.")
        اطبع("  2. Add n days from a date.")
        اطبع("  3. Find weekday of a date.")
        اطبع("  4. Exit the programme.\n")
        اطبع("**Please note the format of date should follow the format of 'DDMMYYYY'\n")
        try:
            خيار = int(ادخال("Select a function: "))
            if خيار == 1:
                التاريخ1 = ادخال("Enter first date (DDMMYYYY): ")
                التاريخ2 = ادخال("Enter second date (DDMMYYYY): ")
                النتيجة = days_between_2_dates(التاريخ1, التاريخ2)
                if النتيجة is not None:
                    اطبع(f"Number of days between dates: {النتيجة}")
                else:
                    اطبع("Invalid date format")
            elif خيار == 2:
                التاريخ = ادخال("Enter date (DDMMYYYY): ")
                عدد_الأيام = int(ادخال("Enter number of days to add: "))
                النتيجة = add_n_days_from_a_date(التاريخ, عدد_الأيام)
                if النتيجة is not None:
                    اطبع(f"Resulting date: {النتيجة}")
                else:
                    اطبع("Invalid date format")
            elif خيار == 3:
                التاريخ = ادخال("Enter date (DDMMYYYY): ")
                النتيجة = weekday_of_date(التاريخ)
                if النتيجة is not None:
                    اطبع(f"Weekday: {النتيجة}")
                else:
                    اطبع("Invalid date format")
            elif خيار == 4:
                انتهى = True
                اطبع("Thank you for using date calculator!")
                break
            else:
                اطبع("Invalid option")
        except ValueError:
            اطبع("Invalid input")
        ادخال("\nPress Enter to continue...")

date_calculator()
