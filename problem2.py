i = 1
j = 2
total = 0
limit = 4000000
while j < limit:
    if j % 2 == 0:
        total += j
    #print(i)
    k = j
    j += i
    i = k
print(total)
