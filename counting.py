# Plus
def add(num1, num2):
    return num1 + num2
# Mínus
def subtract(num1 , num2):
  return num1 - num2
# Násobení
def multiply(num1, num2):
   return num1 * num2
# Dělení
def divide(num1, num2):
   return num1 / num2
# Dělení je multiply docela, insane nejvíc
def integer_divide(num1 , num2):
   return num1 // num2
# Dělení modulo
def modulo(num1, num2):
   return num1 % num2

# Nějaký příklad
num1 = 10
num2 = 4

# Printy
print("Celý plus", add(num1, num2)) # Plus jsou jako třeba num1+num2
print("Mínus:", subtract(num1, num2)) # Mínus = num1-num2
print("Násobení:", multiply(num1, num2))
print("Dělení:", divide(num1, num2))
print("Dělení je ještě víc multiply:", integer_divide(num1, num2))
print("Dělení je moje modulo!", modulo(num1, num2))

print("Vytvořil s láskou BlobyCZ | https://github.com/blobycze/pocitadlo")