# -*- coding: utf-8 -*-
h = float(input('Input your height (M): '))
w = float(input('Input your weight (KG): '))
bmi = w/(h*h)
if bmi <= 18.5:
    print('太轻了, BMI = %.2f' % bmi)  # .2f 表示float保留2位小数
elif 18.5 < bmi <= 25:
    print('很正常, BMI = %.2f' % bmi)
elif 25 < bmi <= 28:
    print('有点胖，要减肥了，BMI = %.2f' % bmi)
elif 28 < bmi <= 32:
    print('太胖了，赶紧的，BMI = %.2f' % bmi)
else:
    print('Woo, 放弃吧, BMI = %.2f' % bmi)
