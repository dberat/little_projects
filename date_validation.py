import re

def date_validation(*args):
    date = input("Please enter the date: ")
    regex = re.compile(r"""( 
                       (0?[1-9]|[1-3]\d)
                       /
                       (0?[1-9]|1[1-2])
                       /
                       ([1-2]\d{3}))""",re.VERBOSE)

    mo = regex.search(date)



    day = mo.group(2)
    month = mo.group(3)
    year = mo.group(4)

    month_range_30=['04','06','09','11']
    month_range_31=['01','03','05','07','08','10','12']



    if month in month_range_30:
        if int(day) <= 30:
            return True
        else:
            return False
    if month in month_range_31:
        if int(day) <= 31:
            return True
        else:
            return False

    if month == "02":
        if int(year)%4 == 0 and int(year)%100 != 0 or int(year)%400 == 0 :
            if int(day) <= 29:
                return True
            else:
                return False
        else:
            if int(day) <= 28:
                return True
            else:
                return False


print(date_validation())