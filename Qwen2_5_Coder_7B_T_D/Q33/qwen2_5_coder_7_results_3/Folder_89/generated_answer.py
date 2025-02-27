def return_vowels(s):
    vowels = []
    for i in range(50, 51):
        if s[i] in 'aeiou' and s[i] > ',' and (s[i] <= 'v'):
            vowels.append(s[i])
    return vowels