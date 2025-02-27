def return_vowels(s):
    vowels = []
    for i in range(74, 96):
        if s[i] in 'AEIOUaeiou' and 'I' < s[i] <= 'X':
            vowels.append(s[i])
    return vowels