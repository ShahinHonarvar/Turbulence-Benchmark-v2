def return_vowels(s):
    vowels = []
    for i in range(29, 73):
        if s[i] in 'aeiou' and '#' < s[i] <= '.':
            vowels.append(s[i])
    return vowels