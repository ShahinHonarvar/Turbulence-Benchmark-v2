def return_vowels(s):
    vowels = []
    for i in range(47, 89):
        if i < len(s) and '@' < s[i] <= 'n' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels