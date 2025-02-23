# Datetime Calculator by Avner

"""PYTHON 函数开始 - 请勿删除 - 由 Avner 制作"""
import math
圆周率 = math.pi
def 打印(*args, **kwargs): print(*args, **kwargs)
def 数字(x): return int(x)
def 小数(x): return float(x)
def 长度(x): return len(x)
def 输入(提示=""): return input(提示)
def 范围(开始, 停止=None, 步=1): return list(range(开始, 停止, 步))
def 总和(迭代, start=0): return start + sum(迭代)
def 任一(迭代): return any(迭代)
def 全部(迭代): return all(迭代)
def 排序(迭代, key=None, reverse=False): return sorted(迭代, key=key, reverse=reverse)
def 反转(迭代): return reversed(迭代)
def 拉链(*迭代): return zip(*迭代)
def 枚举(顺序, start=0): return list(enumerate(顺序, 开始=开始))
def 绝对值(迭代): return abs(迭代)
def 四舍五入(数字, ndigits=None): return round(数字, ndigits)
def 最小值(*args): return min(args[0]) if len(args) == 1 and hasattr(args[0], '__iter__') else min(args)
def 最大值(*args): return max(args[0]) if len(args) == 1 and hasattr(args[0], '__iter__') else max(args)
def 格式化(string, *args, **kwargs): return string.format(*args, **kwargs) if args or kwargs else string
def 字符(迭代): return chr(迭代)
def 顺序(迭代): return ord(迭代)
def 指数(迭代, 指数): return 迭代**指数
def 映射(功能, 迭代, *其他迭代): return list(map(功能, 迭代)) if not 其他迭代 else [功能(*items) for items in zip(迭代, *其他迭代)]
"""PYTHON 函数结束 - 请勿删除 - 由 Avner 制作"""

def is_leap_year(年份):
    return 年份 % 4 == 0 and (年份 % 100 != 0 or 年份 % 400 == 0)

def days_in_month(月份):
    天数列表 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 天数列表[月份]

def num_of_leap_years(起始年份, 结束年份):
    计数 = 0
    for 年份 in range(起始年份, 结束年份):
        if is_leap_year(年份):
            计数 += 1
    return 计数

def is_valid_date(日期):
    if 长度(日期) != 8:
        return False
    try:
        日 = int(日期[:2])
        月 = int(日期[2:4])
        年 = int(日期[4:])
    except ValueError:
        return False
    if 月 < 1 or 月 > 12:
        return False
    最大天数 = days_in_month(月)
    if 月 == 2 and is_leap_year(年):
        最大天数 = 29
    return 1 <= 日 <= 最大天数

def num_of_days_from_1900(日期):
    if not is_valid_date(日期):
        return None
    日 = int(日期[:2])
    月 = int(日期[2:4])
    年 = int(日期[4:])
    天数 = (年 - 1900) * 365 + num_of_leap_years(1900, 年)
    for 月份 in range(1, 月):
        天数 += days_in_month(月份)
    if 月 > 2 and is_leap_year(年):
        天数 += 1
    天数 += 日 - 1
    return 天数

def days_between_2_dates(日期1, 日期2):
    天数1 = num_of_days_from_1900(日期1)
    天数2 = num_of_days_from_1900(日期2)
    if 天数1 is None or 天数2 is None:
        return None
    return 绝对值(天数2 - 天数1)

def add_n_days_after_1900(剩余天数):
    年份 = 1900
    月份 = 1
    日 = 1
    while 剩余天数 >= 366 or (剩余天数 >= 365 and not is_leap_year(年份)):
        if is_leap_year(年份):
            if 剩余天数 >= 366:
                剩余天数 -= 366
                年份 += 1
        else:
            剩余天数 -= 365
            年份 += 1
    while 剩余天数 > 0:
        最大天数 = days_in_month(月份)
        if 月份 == 2 and is_leap_year(年份):
            最大天数 = 29
        if 剩余天数 >= 最大天数:
            剩余天数 -= 最大天数
            月份 += 1
            if 月份 > 12:
                月份 = 1
                年份 += 1
        else:
            日 += 剩余天数
            剩余天数 = 0
    return f"{日:02d}{月份:02d}{年份}"

def add_n_days_from_a_date(日期, 天数):
    if not is_valid_date(日期):
        return None
    总天数 = num_of_days_from_1900(日期) + 天数
    return add_n_days_after_1900(总天数)

def weekday_of_date(日期):
    星期列表 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    天数 = num_of_days_from_1900(日期)
    if 天数 is None:
        return None
    return 星期列表[天数 % 7]

def date_calculator():
    完成 = False
    while not 完成:
        打印("-----------------------------------------")
        打印("Welcome to date calculator")
        打印("  1. Calculate number of days between 2 dates.")
        打印("  2. Add n days from a date.")
        打印("  3. Find weekday of a date.")
        打印("  4. Exit the programme.\n")
        打印("**Please note the format of date should follow the format of 'DDMMYYYY'\n")
        try:
            选项 = int(输入("Select a function: "))
            if 选项 == 1:
                日期1 = 输入("Enter first date (DDMMYYYY): ")
                日期2 = 输入("Enter second date (DDMMYYYY): ")
                结果 = days_between_2_dates(日期1, 日期2)
                if 结果 is not None:
                    打印(f"Number of days between dates: {结果}")
                else:
                    打印("Invalid date format")
            elif 选项 == 2:
                日期 = 输入("Enter date (DDMMYYYY): ")
                天数 = int(输入("Enter number of days to add: "))
                结果 = add_n_days_from_a_date(日期, 天数)
                if 结果 is not None:
                    打印(f"Resulting date: {结果}")
                else:
                    打印("Invalid date format")
            elif 选项 == 3:
                日期 = 输入("Enter date (DDMMYYYY): ")
                结果 = weekday_of_date(日期)
                if 结果 is not None:
                    打印(f"Weekday: {结果}")
                else:
                    打印("Invalid date format")
            elif 选项 == 4:
                完成 = True
                打印("Thank you for using date calculator!")
                break
            else:
                打印("Invalid option")
        except ValueError:
            打印("Invalid input")
        输入("\nPress Enter to continue...")

date_calculator()