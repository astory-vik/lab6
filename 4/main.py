from Word import  Word
from RusEN import RuEnDic
def main():
    w1 = Word("Pattern", {"Шаблон", "Заготовка"})
    dictionary = RuEnDic()
    dictionary.words.append(w1)
    dictionary.ShowTranslate('Pattern')


if __name__ == '__main__':
    main()