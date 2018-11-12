company = {}
n = int(input("Количество компаний: "))
s = 0
for i in range(n):
    companyname = input(str(i+1) + "-я компания: ")
    profit1 = int(input("Прибыль 1 квартала: "))
    profit2 = int(input("Прибыль 2 квартала: "))
    profit3 = int(input("Прибыль 3 квартала: "))
    profit4 = int(input("Прибыль 4 квартала: "))
    profit = profit1+profit2+profit4+profit3
    company[companyname] = profit
    s += profit
 
profitis = s / n
print("\nСредняя прибыль компаний составила: %.0f. Компании с прибылью выше среднего:" % profitis)


for i in company:
    if company[i] > profitis:
        print(i)
    if company[i] < profitis:
        print("Компании с прибылью ниже среднего: ", i)