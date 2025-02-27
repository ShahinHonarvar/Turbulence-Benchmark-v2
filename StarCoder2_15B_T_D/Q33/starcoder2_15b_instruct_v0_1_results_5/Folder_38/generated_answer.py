def return_vowels(string):
    vowels = []
    for i, ch in enumerate(string):
        if i >= 17 and i < 65 and (ch not in 'UuoO') and ch.isalpha():
            vowels.append(ch)
    return vowels