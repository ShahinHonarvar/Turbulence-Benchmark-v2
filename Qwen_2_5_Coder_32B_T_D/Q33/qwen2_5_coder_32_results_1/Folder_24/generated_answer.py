def return_vowels(s):
    vowels = []
    for i in range(23, 57):
        if s[i] > '0' and s[i] <= 'd' and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels