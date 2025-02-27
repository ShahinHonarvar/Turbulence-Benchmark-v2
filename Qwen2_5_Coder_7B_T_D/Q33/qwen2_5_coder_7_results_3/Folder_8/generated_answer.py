def return_vowels(s):
    vowels = []
    for i in range(64, 82):
        if s[i] in 'AEIOUaeiou' and s[i] > 'P' and (s[i] <= 'z'):
            vowels.append(s[i])
    return vowels