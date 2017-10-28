def checkio(array):

    
    ans=0

    if len(array)==0:
        return 0
    else:
               
        for i,item in enumerate(array):
            #print (array.index(i))
            if i%2==0:
                ans +=item


        anss = ans*array[-1]         
        return anss


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")






def checkio(number):
    ans=1
    for el in str(number):
        if int(el)>0:
            #print (num)
            ans*=int(el)
            
    return ans
        
           
     

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")














def find_message(text):
    
    stroka_list = list(text)
    #print (stroka_list)
    ans=""
    if text.islower():
        #print("asdasdasd")
        ans=""
        return ans
    else:


        for i in stroka_list:
            #print (i)

            if i.isupper():
                ans=str(ans + i)
            
        #print (ans)
        return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")    










'''def most_frequent(data):
    
    my_dict = {}
    for i in data:
        my_dict[i]= data.count(i)
        #print (my_dict)

    my_max_key = max(my_dict.values())
    ans=my_max_key
    #print (my_max_key)

    new_list = []
    for key in my_dict:
        if my_dict[key]==ans:
            new_list.append(key)
    return new_list[0]  


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')   ''' 






def most_frequent(data):
    
    
    a = 0
    b = 0
    cur = data[0]
    for i, k in enumerate(data):
    
        a = data.count(k)
    
        if b < a:
    
            b = a
            cur = data[i]
    return cur  

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
