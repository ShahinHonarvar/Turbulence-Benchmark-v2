def return_vowels(s):
    vowels = []
    for i in range(44, 95):
        if s[i] in 'aeiou' and s[i] > '5' and (s[i] <= '<'):
            vowels.append(s[i])
    return vowels