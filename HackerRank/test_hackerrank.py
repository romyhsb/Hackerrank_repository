def reverse_words_order_and_swap_cases(sentence):
    value = sentence.split()
    result = []
    word = ''
    for i in value:
        for j in i:
            if j.isupper():
                word+=j.lower()
            elif j.islower():
                word+=j.upper()
        result.append(word)
        word = ''
    print(' '.join(result[::-1]))

reverse_words_order_and_swap_cases("aWESOME is Coding")