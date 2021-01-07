print("\n  PROGRAM TO PRINT HCF OF TWO NUMBERS \n")

a=int(input("  ENTER THE FIRST NUMBER : "))
b=int(input("  ENTER THE SECOND NUMBER : "))
c=a+b
hcf=0
for i in range(1,a+1):
    if (a%i==0 and b%i==0):
        hcf=i

print("\n  HCF OF TWO NUMBERS IS : ",hcf)