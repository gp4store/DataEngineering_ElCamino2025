# Gerardo
# Pastore
# 2025-01-02-de-eastern
# submission date

try:

    list1 = ['1', '2', [3]]
    list1[2] = list1[2][0]
    list2 = [('3', 4), '5', 6]
    list2 = list(list2[0]) + list2[1:]
    list3 = list1 + list2
    
    odds_evens = {'odds': [], 'evens': []}
    for i in list3:
        num = int(i)
        if num % 2 == 0:
            odds_evens['evens'].append(i)
        else:
            odds_evens['odds'].append(i)

except ZeroDivisionError:
    print('One item in your list is zero, cant divide by zero')
else:
    print(odds_evens)
    numbers = [int(k) for k in list3]
    all_integers = { k: [int(v) for v in val] for k, val in odds_evens.items()}

    highestnum = max(numbers)
    numbers += [int(item) + highestnum for values in odds_evens.values() for item in values]

finally:
    print(sorted(set(numbers)))