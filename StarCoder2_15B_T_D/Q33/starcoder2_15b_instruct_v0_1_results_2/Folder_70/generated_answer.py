def return_vowels(string):
    vowels = []
    for i in range(171, 402):
        c = string[i]
        if c.isalpha() and c.lower() in 'aeiou' and (c > 'I') and (c <= 'k'):
            vowels.append(c)
    return vowels