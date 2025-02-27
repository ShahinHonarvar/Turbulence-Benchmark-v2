def return_vowels(s):
    vowels = []
    for i in range(56, 96):
        if 'a' < s[i] <= 'T' and s[i] in 'aeiou':
            vowels.append(s[i])
    return vowels