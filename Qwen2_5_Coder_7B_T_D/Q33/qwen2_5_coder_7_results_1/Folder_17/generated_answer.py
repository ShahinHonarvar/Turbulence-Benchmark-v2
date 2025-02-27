def return_vowels(s):
    vowels = []
    for i in range(60, 99):
        if s[i] in 'aeiou' and 'j' < s[i] <= 'n':
            vowels.append(s[i])
    return vowels