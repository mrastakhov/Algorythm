#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите целое трехзначное число : '))

b = a%10

c = a%100//10

d = a//100

e = b*c*d

f = b+c+d


print(e,f)
