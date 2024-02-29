a=int(input())
A=[a%10, a//10-a//100*10, a//100]
ne=sum(A)-max(A)-min(A)
if ne==(max(A)+min(A))/2:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")