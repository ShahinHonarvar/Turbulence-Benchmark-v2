def return_vowels(s):
    vowels = []
    for i in range(1, 4):
        if 'C' < s[i] <= 'I' and s[i] in 'AEIOU':
            vowels.append(s[i])
    return vowels