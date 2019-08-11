# Class for counting letters in a phrase or sentence.
class count_letters:
    def letter_count(word):
        word_c=word
        i=0
        for x in word:
            i+=1
            if ' ' in x:
                i-=1
        return i

# Class for counting words in a phrase or sentence.
class count_words:
    def word_count(word):
        word_c=word.split()
        i=0
        for x in word_c:
            i+=1
        return i

# This class in an inheritance class.
class word_count(count_words):
    pass