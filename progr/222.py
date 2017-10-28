#!/usr/bin/env python
# encoding: utf-8

'''def checkio(text):
    total = 0
    print (total)
    lower = text.lower()
    print ("lower_is"+ ' '+ lower)
    most = lower[0]
    print ("most_is"+ ' '+ lower)
    for i in lower:
    	print (lower.count(i))
    	most = i
    	print ("most_is"+ ' '+  most)

    	
        #if i.isalpha():
            #if lower.count(i) > total:
             #   most = i
#
 #               total = lower.count(i)
#
 #           elif lower.count(i) == total:
  #              if i < most:
   #                 most = i
    #                total = lower.count(i)
    print (most)
    
   
    
        
    #replace this for solution
    return 'a'
 


if __name__ == '__main__':
	checkio("priivet")
	'''


#dict = {}
#print (dict)
#dict = {"01":"Янвварь","02":"Февраль","03":"Март","04":"Апрель","05":"Май","06":"Июнь","07":"Июль","08":"Август","09":"Сентябрь","10":"Октябрь","11":"Ноябрь","12":"Декабрь"} 
#print (dict["01"])


#s = {1, 2, 3}
#if 3 in s:
#    print ("PRIVET")
#if 5 not in s:
#    s.add(6)
#    print (s)


#d = {42:"bar", "foo":1}
#print (d)

#import traceback
#d = {}
#try:
#    d["foo"]
#except Exception as exc:
#    print (traceback.format_exc())





#import random
#a = [random.randint(-10, 10) for i in range(10)]
#b = [item ** 2 for item in a if item > 0]
#print (b)


#a=0
#if a==0:
#    print (a)
#else:
#    a+=a
#    print(a)


#Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
#затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.


#def checkio(array):

#array = [-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]
#ans=0

#if len(array)==0:
#    print (0)
#else:
#    for i,item in enumerate(array):
#        #print(i,item)
#        #print (array.index(i))
#        if i%2==0:
#            print (item)
#            ans +=item
#    #print (123, ans)
#    print (321,array[-1])

#    anss = ans*array[-1]         
#    #return anss
#    print (anss)


   #41*(-37-19+29+3-64+36+26+55+84-65)


#if __name__ == '__main__':
   
#    assert checkio([-89,-86,13,-69,94,-75,66,97,-50])== 1700, "(0+2+4)*5=30"
 #   assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
  #  assert checkio([6]) == 36, "(6)*6=36"
   # assert checkio([]) == 0, "An empty array = 0"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")






#Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

#Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".

#Входные данные: Текст как строка (юникод).

#Выходные данные: Секретное сообщение как строка или пустая строка.




#def find_message(text):
#    stroka = "How are you? Eh, ok. Low or Lower? Ohhh."
#    stroka_list = list(stroka)
#    #print (stroka_list)
#    ans=""
##    if stroka.islower():
 #       #print("asdasdasd")
 #       ans='""'
 #       return ans
 #   else:#


        #for i in stroka_list:
        #    #print (i)

            #if i.isupper():
             #   ans=str(ans + i)
            
        #print (ans)
        #return ans


    

#if __name__ == '__main__':
#    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
#    assert find_message("hello world!") == "", "Nothing"
#    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")









#Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).



#def checkio(number):
#    ans=1
#    for el in str(number):
#        if int(el)>0:
#            #print (num)
#            ans*=int(el)
#            
#    return ans
#        
           
     

#if __name__ == '__main__':
#    assert checkio(123405) == 120
##    assert checkio(999) == 729
 #   assert checkio(1000) == 1
 #   assert checkio(1111) == 1
 #   print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")










#def most_frequent(data):
'''
data=['a', 'a']
a=0
b=0
if len(data)==1:
    print (data[0])
else:
    for i,k  in enumerate (data):
        #print (i,k)
        a=data.count(k)
        print(a)
        if b<a:
            b=a

    print (b)    
    print (data[b])


    #print (i)
  
        #determines the most frequently occurring string in the sequence.
    
    # your code here
    #return None






#if __name__ == '__main__':
#    #These "asserts" using only for self-checking and not necessary for auto-testing
#    assert most_frequent([
#        'a', 'b', 'c', 
#        'a', 'b',
#        'a'
#    ]) == 'a'

#    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
#    print('Done')

'''

#b = [a ** 3 for i in range(-10,10) if a % 3==0]
#print (b)





#from collections import Counter

#def most_fre(strings):
#    return Counter(strings).most_common(1)[0][0]




#создается там же где лежит файл .py


#with open("C://Python3//test.txt", "w") as testfile:
#    testfile.write("привет\n")


#with open("test.txt","r") as testfile2:
#    a = testfile2.read()
#    print(a)

#with open ("test.txt", "r") as testfile3:
#    for line       


import os  #создание
a = os.getcwd()
os.mkdir()
os.rmdir()
os.listdir()
os.makedirs("testdir/some_dir/somes")
os.remove()


print (a)


import shutil
shutil.copytree()
shutil.rmtree() удалить все дерево целиком
shutil.copyfile()
shutil.remove()


import sys

sys.argv() аргусенты с которыми передается программа
sys.stdin() поток ввода
sys.stdout() поток вывода
sys.stderr() поток ошибок



for i in sys.stdin:
    print (line.split("")[0])




import subprocess

proc = subprocess.Popen("ls", stdout = subprocess.PIPE. stdin = subprocess.PIPE)
outs, errs = proc.communicate()
print (outs)
print (errs)















