"""
Rozwiązanie: 
(A) What is the maximal number of people affected (in worst case scenario)?
8: 
jest to dzielenie binarne:
1 osoba piję z przedziału [1,500]
Jeżeli ma objawy to butelka jest w [1,500]
Jeżeli nie ma to butelka jest w [501,1000]
2 osoba pije z przedzialu, gdzie byla zakazona butelka dzielac ten przedzial na polowe [0,500] albo [501,1000]
Czyli pije z przedzialu 
[1,125] lub [126,500] lub [501,750] lub [751, 1000]
I w tym kroku wiemy w ktorym przedziale jest butelka zakazona. 
itd. 

Najgorszy scenariusz jest wtedy, kiedy za każdym razem kolejna osoba trafia na zakazona butelkę
Założmy, że pierwsza osoba trafiła w [1,500] 
kolejna trafila w [1,125]
kolejna trafila w [1,62]
kolejna trafila w [1,31]
kolejna trafila w [1,15]
kolejna trafila w [1,7]
kolejna trafila w [1,3]
kolejna trafila w [1,1]
pesymistyczny: w 9 krokach mamy pewność, gdzie będzie butelka zakazona 
"""

def binary_search(arr, l ,r, number, licznik):
    if r >= l:
        mid = l + (r -l) // 2
      
        licznik += 1
        if arr[mid] == number:
            print("Person have bottle".format(number))
            return mid
        elif arr[mid] > number:
            print(" Person will {0} drink from bottles".format(licznik))
            print([x for x in range(l, mid)])

            return binary_search(arr, l, mid -1, number, licznik)
        else: 
            print(" Person will {0} drink from bottles".format(licznik))
            print([x for x in range(mid + 1, r+1)])

            return binary_search(arr, mid + 1, r, number, licznik)
        
    else:
        return None

binary_search(range(0,1000), l=0, r=1000, number=123, licznik=0)