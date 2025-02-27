def return_vowels(s):
    vowels = []
    for i in range(604, 949):
        if s[i] in 'AEIOU' and 'N' < s[i] <= 'U':
            vowels.append(s[i])
    return vowels