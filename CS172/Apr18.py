a = [5, 4, 3, 2, 1, 0]
i = 0

n = len(a)
x = 1
j = i+1
while j < n:
    if a[j] < a[x]:
        x = j
    j += 1
a[i], a[x] = a[x], a[i]