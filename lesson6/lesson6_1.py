try:
    height = int(input("請輸入身高(cm):"))
    if height < 120 or height > 220:
        raise Exception(f'您輸入的{height},不在120~220範圍內')
    weight = int(input("請輸入體重(kg):"))
    if weight < 20 or weight > 200:
        raise Exception(f'您輸入的{weight},不在20~200範圍內')
    height /= 100
    bmi = weight/height**2
except ValueError:
    print("輸入發生錯誤")
except Exception as e:
    print(e)
else:
    print(f'您的BMI為{bmi:.2f}')
    if bmi < 18.5:
        print("體重過輕")
    elif bmi < 24:
        print("正常範圍")
    elif bmi < 27:
        print("過重")
    elif bmi < 30:
        print("輕度肥胖")
    elif bmi < 35:
        print("中度肥胖")
    else:
        print("重度肥胖")