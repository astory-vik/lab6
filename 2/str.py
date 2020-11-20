import re


class NewString(str):

    def Chars3(self, s):
        regex = re.compile(r'^.*(.)(\1)(\1).*$')
        if regex.match(s):
            return True
        else:
            return False

    def IsPalindrome(self, S):
        if len(S) <= 1:
            return True
        else:
            return S[0] == S[-1] and self.IsPalindrome(S[1:-1])
