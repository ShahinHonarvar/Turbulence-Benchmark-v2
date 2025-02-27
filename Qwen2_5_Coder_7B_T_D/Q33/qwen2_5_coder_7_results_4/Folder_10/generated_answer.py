def return_vowels(s):
    vowels = []
    for i in range(31, 37):
        if 59 < ord(s[i]) <= 116 and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels