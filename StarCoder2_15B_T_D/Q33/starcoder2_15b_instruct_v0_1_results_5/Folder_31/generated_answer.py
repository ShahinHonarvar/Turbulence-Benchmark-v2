def return_vowels(string):
    vowels = []
    for c in string:
        if c in 'aeiou' and string.index(c) >= 65 and (string.index(c) < 70) and (c > '%') and (c <= 'G'):
            vowels.append(c)
    return vowels