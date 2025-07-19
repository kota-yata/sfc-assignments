from datetime import *

year = int(input("西暦年を入力："))
month = int(input("月を入力："))

cal = date(year, month, 1)  # その年月の1日を指定します
print(cal.strftime("%B %Y"))
print("Sun Mon Tue Wed Thu Fri Sat")
startday = cal.weekday()  # 月曜日=0, 日曜日=6

# 日曜日=0に調整します
startday = (startday + 1) % 7

for _ in range(startday):
    print("   ", end=" ")

if month == 2: 
    limitday = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28  # 閏年の場合かどうか判定してください
else:
    limitday = 30 if month in [4, 6, 9, 11] else 31  # 大の月・小の月を判定してください

for day in range(1, limitday + 1):
    print(f" {day:2}", end=" ")
    if (startday + day) % 7 == 0: 
        print()
print()
