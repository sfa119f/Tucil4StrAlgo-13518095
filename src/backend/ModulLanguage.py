import nltk

def SplitSentence(paragraph):
    sentence = nltk.sent_tokenize(paragraph)
    return sentence

def LowerCase(sentence):
    sentence = sentence.lower()
    return sentence