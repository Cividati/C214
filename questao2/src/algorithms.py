def wordCount(frase):
    return len(frase.split(' '))

def pairWords(frase):
    array_frase = frase.split(' ')
    num_pair_words = 0

    for i in array_frase:
        if len(i)%2 == 0:
            num_pair_words+=1 
    return num_pair_words
