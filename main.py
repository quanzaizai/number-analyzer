raw_text = input("请输入一组整数，数字之间用空格隔开：")

parts = raw_text.split()
numbers = []

for p in parts:
    numbers.append(int(p))

total_count = 0
even_count = 0
odd_count = 0
big_total = 0

for n in numbers:
    total_count = total_count + 1

    if n % 2 == 0:
        even_count = even_count + 1

    if n % 2 != 0:
        odd_count = odd_count + 1

    if n > 10:
        big_total = big_total + n

print("原始数字列表:", numbers)
print("总个数:", total_count)
print("偶数个数:", even_count)
print("奇数个数:", odd_count)
print("大于10的数字总和:", big_total)
print("Git is watching my changes.")
