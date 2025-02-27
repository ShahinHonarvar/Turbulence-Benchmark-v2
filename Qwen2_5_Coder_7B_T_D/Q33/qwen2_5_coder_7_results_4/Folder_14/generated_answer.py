def return_vowels(s):
    vowels = []
    for i in range(47, 61):
        if s[i] in 'AEIOU' and 9 < ord(s[i]) <= ord('O'):
            vowels.append(s[i])
    return vowels