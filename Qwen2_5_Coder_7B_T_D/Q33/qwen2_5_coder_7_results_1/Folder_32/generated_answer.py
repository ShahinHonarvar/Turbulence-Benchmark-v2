def return_vowels(s):
    vowels = []
    for i in range(45, 76):
        if s[i] in 'aeiou' and 'b' < s[i] <= 'z':
            vowels.append(s[i])
    return vowels