def prime(num):
     for i in range(2,round(num/2)):
          if(num%i==0):
               print("not prime")
               return
     print("prime")
prime(33)