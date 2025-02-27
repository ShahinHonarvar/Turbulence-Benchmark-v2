def return_vowels(s):
    vowels = []
    for i in range(23, 85):
        if s[i] in 'aeiou' and 'W' < s[i] <= 'v':
            vowels.append(s[i])
    return vowels