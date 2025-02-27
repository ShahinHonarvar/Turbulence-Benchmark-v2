def return_vowels(string):
    vowels = []
    for i, c in enumerate(string):
        if c in 'aeiou' and 21 <= i < 59 and (c > '/') and (c <= 'a'):
            vowels.append(c)
    return vowels