from sympy.ntheory.factor_ import totient
  
n = 152416431947009
  
phi_n = totient(n) 
      
print("φ({}) = {} ".format(n, phi_n))