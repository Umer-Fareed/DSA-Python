#Find fibonacci sequence
reputations= int(input('how much time to run? \n'))
prev1= 0
prev2= 1

for _  in range(reputations):
    newfibo= prev1 + prev2
    print(newfibo)
    prev1= prev2
    prev2= newfibo
