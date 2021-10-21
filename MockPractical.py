net_amount=0
while(net_amount<=0):
  while input("Enter y to continue: ")=="y":
    a = input("Enter input: ")
    trans = a.split(" ")
    b=trans[1]
    amt=int(trans[0])
    
    if b=="d":
      net_amount+=amt 
    elif b=="w":
      net_amount-=amt 
    else:
      pass
print("Total Balance:", net_amount)
