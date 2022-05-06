import random
import string
from operator import length_hint
from symtable import Symbol
def main():
    print("Welcome to Random Password Generator:\n")
    length = int(input("Enter the length of password you want:\n"))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    SymbolD =string.punctuation
    combine=lowerD+upperD+digitD+SymbolD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()