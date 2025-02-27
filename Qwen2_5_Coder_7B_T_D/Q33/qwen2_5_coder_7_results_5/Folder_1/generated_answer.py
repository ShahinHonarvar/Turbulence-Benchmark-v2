def return_vowels(s):
    vowels = []
    for i in range(24, 64):
        if s[i] in 'aeiou' and 'F' < s[i] <= 'h':
            vowels.append(s[i])
    return vowels