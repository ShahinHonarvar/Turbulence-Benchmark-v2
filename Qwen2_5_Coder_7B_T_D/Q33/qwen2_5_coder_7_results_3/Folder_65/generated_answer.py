def return_vowels(s):
    vowels = []
    for i in range(71, 88):
        if s[i] in 'aeiou' and 9 < ord(s[i]) <= ord('P'):
            vowels.append(s[i])
    return vowels