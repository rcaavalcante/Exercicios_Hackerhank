''' Ordem definida
 - Letras minúsculas devem vir primeiro e ser classificadas.
 - Letras maiúsculas devem vir depois e ser classificadas.
 - Dígitos ímpares devem vir depois das letras maiúsculas e ser classificados.
 - Dígitos pares devem vir por último e ser classificados. '''

import sys
def sort_string(S):
   # Initialize lists for different categories
   lowercase_letters = []
   uppercase_letters = []
   odd_digits = []
   even_digits = []

   # Classify each character in the string S
   for char in S:
       if char.islower():
           lowercase_letters.append(char)
       elif char.isupper():
           uppercase_letters.append(char)
       elif char.isdigit():
           digit = int(char)
           if digit % 2 == 1:
               odd_digits.append(char)
           else:
               even_digits.append(char)

   # Sort each list
   lowercase_letters.sort()
   uppercase_letters.sort()
   odd_digits.sort()
   even_digits.sort()

   # Concatenate all sorted parts
   sorted_string = ''.join(lowercase_letters + uppercase_letters + odd_digits + even_digits)

   return sorted_string


if __name__ == "__main__":
   input = sys.stdin.read().strip()
   print(sort_string(input))


