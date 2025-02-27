def return_vowels(string):
    vowels = []
    for c in string:
        if c.isalpha() and c.lower() in 'aeiou' and (32 < ord(c) < 97) and (c > 'Q') and (c <= ']'):
            vowels.append(c)
    return vowels