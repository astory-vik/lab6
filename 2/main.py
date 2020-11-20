from str import NewString

def Main():
    myS = NewString()
    s = input("Enter string")
    print(myS.Chars3(s))
    print(myS.IsPalindrome(s))
if __name__ == '__main__':
    Main()