def return_vowels(s):
    vowels = []
    for i in range(56, 90):
        if s[i] in 'aeiou' and 'K' < s[i] <= 'z':
            vowels.append(s[i])
    return vowels