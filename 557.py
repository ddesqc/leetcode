# Reverse Words in a String III
def reverse_word(word):
    return word[::-1]

def reverse_sentence(sentence):
    reversed_sentence = ""
    # words = sentence.replace(" ","* *")
    words = sentence.replace(" ","* *").split('*')
    for word in words:
        reversed_sentence += word[::-1]
    return reversed_sentence


print(reverse_sentence("Bonjour com2ment ça va - ?"))