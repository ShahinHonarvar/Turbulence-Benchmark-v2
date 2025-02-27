def return_vowels(s):
    vowels = []
    for i in range(37, 57):
        if s[i] in 'aeiou' and '*' < s[i] <= 'P':
            vowels.append(s[i])
    return vowels