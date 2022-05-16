def dvigenere(coded, key, alph = 'abcdefghijklmnopqrstuvwxyz0123456789'):
    keyphrase = ''
    count = 0
    decoded = ''
    coded = coded.lower()
    for index in range(len(coded)):
        if coded[index] in alph:
            keyphrase += key[(count)%len(key)]
            count += 1
        else:
            keyphrase += coded[index]
    for index in range(len(coded)):
        if coded[index] in alph:
            i = alph.find(coded[index]) - alph.find(keyphrase[index])
            decoded += alph[i%36]
        else:
             decoded += coded[index]
    return decoded

def cvigenere(decoded, key, alph = 'abcdefghijklmnopqrstuvwxyz0123456789'):
    keyphrase = ''
    count = 0
    coded = ''
    decoded = decoded.lower()
    for index in range(len(decoded)):
        if decoded[index] in alph:
            keyphrase += key[(count)%len(key)]
            count += 1
        else:
            keyphrase += decoded[index]
    for index in range(len(decoded)):
        if decoded[index] in alph:
            i = alph.find(decoded[index]) + alph.find(keyphrase[index])
            coded += alph[i%36]
        else:
             coded += decoded[index]
    return coded
