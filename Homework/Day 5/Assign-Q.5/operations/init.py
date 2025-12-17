import arithmetic as ar
import string_ops as s
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition: ", ar.add(a,b))
print("Multiplication: ",ar.multiply(a,b) )

text = input("Enter the text: ")
print(f"Reverse string ={s.reverse_string(text)}")
print(f"vowel = {s.count_vowels(text)}")
