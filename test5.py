# -*- coding: cp1252 -*-
def sum_of_multiples(limit):
    count = 0
    sum = 0
    multiples = []

    while count <= limit:
    if count % 3 == 0 and count not in multiples:
        multiples.append(count)
    print(count)
    elif count % 5 == 0 and count not in multiples:
    multiples.append(count)
    print(count)
    count+=1
    for each in multiples:
    sum +=each
    print("\nSum is " + str(sum))

    limit = int(input("Enter the limit: "))
    sum_of_multiples(limit)
