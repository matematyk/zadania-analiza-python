def sorted_set_sum(list1, list2):
    wynik = []
    n = min(len(list1), len(list2))
    i = 0 
    j = 0
    while i < n or j < n:
        if list1[i] < list2[j]:
            wynik.append(list1[i])
            i = i + 1
        elif list1[i]  == list2[j]:
            wynik.append(list1[i])
            i = i + 1
            j = j + 1
        else:
            wynik.append(list2[j])
            j = j + 1
    if n == 0:
        n = -1
    if len(list1) == max(len(list1), len(list2)):
        for i in range(n+1, len(list1)):
            wynik.append(list1[i])
    if len(list2) == max(len(list1), len(list2)):
        for i in range(n+1, len(list2)):
            wynik.append(list2[i])
    return wynik


print(sorted_set_sum([], []) == [])
print(sorted_set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3])
print(sorted_set_sum([], [1, 2, 3]) == [1, 2, 3])
print(sorted_set_sum([1, 2, 3], []) == [1, 2, 3])

print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]) == [-3, -2, 0, 1, 3, 34])
