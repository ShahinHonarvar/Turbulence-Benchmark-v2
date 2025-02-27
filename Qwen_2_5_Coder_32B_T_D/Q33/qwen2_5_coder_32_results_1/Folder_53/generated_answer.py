def return_vowels(s):
    vowels = []
    for i in range(27, 57):
        if s[i] in 'aeiou' and 'o' < s[i] <= 'w':
            vowels.append(s[i])
    return vowels