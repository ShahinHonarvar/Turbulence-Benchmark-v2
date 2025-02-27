def return_vowels(s):
    vowels = []
    for i in range(63, 79):
        if i < len(s) and s[i] in 'aeiou' and ('D' < s[i] <= 'y'):
            vowels.append(s[i])
    return vowels