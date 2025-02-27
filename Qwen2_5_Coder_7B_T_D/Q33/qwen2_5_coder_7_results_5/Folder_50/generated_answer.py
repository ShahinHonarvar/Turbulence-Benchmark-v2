def return_vowels(s):
    vowels = []
    for i in range(11, 53):
        if s[i] in 'aeiou' and '+' < s[i] <= 'W':
            vowels.append(s[i])
    return vowels