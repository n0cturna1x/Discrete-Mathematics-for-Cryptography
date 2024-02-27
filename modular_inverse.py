def modular_inverse(a,b):

    for i in range(1,b):
        if((a%b)*(i%b) % b==1):
            return i
    raise Exception('The modular inverse does not exist.')

a = 3761
b = 31363

try:
    result=modular_inverse(a,b)
    print(f"Modular inverse of {a} mod {b}: "+ str(result))
except:
    print(f'{a} mod {b}: The modular inverse does not exist.')