raw_text = input("请输入一串数字:")
if raw_text.strip() == "" :
    print("请至少输入一个整数数据")
else:
 try:
    parts = raw_text.split()
    numbers = []

    for text_num in parts:
        numbers.append(int(text_num))
    total_count = 0
    even_count = 0
    odd_count = 0
    big_count = 0
    big_sum = 0
    total_sum = 0

    for num in numbers:
        total_count = total_count + 1
        total_sum = total_sum + num

        if num % 2 == 0:
            even_count = even_count + 1

        if num % 2 != 0:
            odd_count = odd_count + 1

        if num > 10:
            big_count = big_count + 1
            big_sum = big_sum + num

    average = total_sum / total_count

    print("输出原始数据列表：", numbers)
    print("数量个数：", total_count)
    print("数量总和：", total_sum)
    print("偶数个数：", even_count)
    print("奇数个数：", odd_count)
    print("大于10的数字的个数:", big_count)
    print("大于10的数的总和:", big_sum)
    print("这些总数的平均数为：", average)

 except:
     print("请输入整数，并用空格隔开")