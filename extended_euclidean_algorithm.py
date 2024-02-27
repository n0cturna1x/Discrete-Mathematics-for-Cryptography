def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x
 
if __name__ == '__main__':
 
    gcd, x, y = extended_euclidean_algorithm(56343, 2072)
    print('gcd(56343, 2072) = ', gcd)
    print(f'x = {x}, y = {y}')
    
    gcd, x, y = extended_euclidean_algorithm(31363, 3761)
    print('\ngcd(31363, 3761) = ', gcd)
    print(f'x = {x}, y = {y}')