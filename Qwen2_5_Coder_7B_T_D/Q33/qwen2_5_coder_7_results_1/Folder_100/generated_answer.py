def return_vowels(s):
    vowels = []
    for i in range(23, 75):
        if s[i] in 'aeiou' and 'L' < s[i] <= 'd':
            vowels.append(s[i])
    return vowels