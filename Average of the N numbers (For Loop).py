n = int(input())
count = 0
for i in range(1, n+1):
    result = i + count 
    count = result
print(result / n)