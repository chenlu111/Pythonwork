str='X-DSP AM-Confidence:0.8475'
#print(str.find(':'))
n=str[(str.find(':')+1):]

f=float(n)

print(f)