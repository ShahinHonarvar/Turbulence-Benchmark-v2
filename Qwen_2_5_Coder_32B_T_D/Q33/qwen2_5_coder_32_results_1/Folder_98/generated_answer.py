def return_vowels(s):
    vowels = []
    for i in range(3, 9):
        if s[i] in 'AEIOU' and 'S' < s[i] <= 'U':
            vowels.append(s[i])
    return vowels