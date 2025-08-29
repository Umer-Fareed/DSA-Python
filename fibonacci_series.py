#Find fibonacci sequence
prev1= 0
prev2= 1

for fibo in range(18):
    newfibo= prev1 + prev2
    print(newfibo)
    prev1= prev2
    prev2= newfibo
