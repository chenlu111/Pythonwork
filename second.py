num=input('Enter your numbers:')

num=list(map(int,num.split()))

a=max(num)
b=min(num)

print('max=%d'%a)
print('min=%d'%b)