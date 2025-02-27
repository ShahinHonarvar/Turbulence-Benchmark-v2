def return_vowels(s):
    vowels = []
    for i in range(85, 99):
        if i < len(s) and '/' < s[i] <= 'n' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels