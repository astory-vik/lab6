class RuEnDic:
    words = []
    def ShowTranslate(self, word):
        k = 0
        for i in self.words:
            if i.word == word:
                print(self.words[k].translate)
            k +=1
