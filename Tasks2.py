import random

#------Random list

n = 10
a = [0]*n
for i in range(n):
    a[i] = random.randint(-10, 10)
print(a)

#-------Positive numbers from list a

b = []

for i in range(n):
    if a[i] > 0:
        b.append(a[i])

print(b)

#--------Changing the order in list a

for i in range(n//2):
    temp = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = temp
    
print(a)

#--------Fibonacci sequence

num = 20
fibs = [0, 1]

for i in range(2, num):
    fibs.append(fibs[i - 1] + fibs[i - 2])
                
print(fibs)

#---------Counting letters in a string

strng1 = "Вот, эм, всей швали моих критиков, моих завистников. Вы думаете, что с человеком, который вот до такой степени точно исследует тему, можно спорить? Вы думаете что я вас не переиграю? Что я вас не уничтожу? Я вас уничтожу"
def search_letter(s):
    ch = input("Введите букву: ")
    count = 0
    for i in range(len(s)):
        if s[i].lower() == ch:
            count += 1
    return count
print(search_letter(strng1))

#----------Counting words in a string

strng2 = "Вот, эм, всей швали моих критиков, моих завистников. Вы думаете, что с человеком, который вот до такой степени точно исследует тему, можно спорить? Вы думаете что я вас не переиграю? Что я вас не уничтожу? Я вас уничтожу"
def search_word(s):
    ch = input("Введите слово: ")
    count = 0
    ch_len = len(ch)
    timer = 0
    for i in range(len(s)):
        if s[i].lower() == ch[0]:
            timer += 1
            while (ch_len - 1 > 0):
                if(s[i + timer] != ch[timer]):
                    break;
                else:
                    ch_len -= 1
            timer = 0
            count += 1
    return count
print(search_word(strng2))

































    
        
