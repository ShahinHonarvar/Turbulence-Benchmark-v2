def return_vowels(s):
    vowels = []
    for i in range(464, 574):
        if s[i] in 'aeiou' and 'a' < s[i] <= 'g':
            vowels.append(s[i])
    return vowels