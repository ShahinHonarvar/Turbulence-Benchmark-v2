def return_vowels(text):
    vowels = []
    for i in range(len(text)):
        if i >= 3 and i < 9 and (text[i] in 'AEIOU') and (text[i] > 'S') and (text[i] <= 'U'):
            vowels.append(text[i])
    return vowels