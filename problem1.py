total = 0
i = 0
done = False
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1

print(total)
