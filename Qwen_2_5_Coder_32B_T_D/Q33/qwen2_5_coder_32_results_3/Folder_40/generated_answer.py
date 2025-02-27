def return_vowels(s):
    vowels = []
    for i in range(2, 7):
        if s[i] > '^' and s[i] <= 'd' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels