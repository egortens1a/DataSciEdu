# put your python code here
s,t = input(), input()
count = 0
pos = 0
while s.find(t) != -1:
    count+=1
    s = s[s.find(t)+1:]
print(count)


