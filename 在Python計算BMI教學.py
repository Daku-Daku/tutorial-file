import math
height = float(input("請輸入身高(米)："))
weight = float(input("請輸入體重(公斤)："))
bmi = round(weight/math.pow(height, 2), 2)
description = ["體重嚴重過輕", "體重中度過輕", "體重輕度過輕", "體重正常", "輕度肥胖", "中度肥胖", "嚴重肥胖"]
if bmi < 15:
    result = description[0]
elif 15 <= bmi < 16:
    result = description[1]
elif 16 <= bmi < 18.5:
    result = description[2]
elif 18.5 <= bmi < 25:
    result = description[3]
elif 15 <= bmi < 30:
    result = description[4]
elif 30 <= bmi < 35:
    result = description[5]
elif 35 <= bmi < 40:
    result = description[6]
elif bmi > 40: 
    result = description[7]
print("您的BMI指數為：{}，{}".format(bmi, result))