def return_vowels(s):
    vowels = []
    for i in range(21, 23):
        if 97 <= ord(s[i]) <= 110 and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels