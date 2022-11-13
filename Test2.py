Fulllist = list(range(1, 101))
even = []
for num in Fulllist:
    if (num % 2) == 0 :
        even.append(num)
even.append("true")
print (even)
print (even[:10])
print (len(even))
