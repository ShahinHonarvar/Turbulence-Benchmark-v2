def return_vowels(s):
    vowels = []
    for i in range(47, 61):
        char = s[i]
        if char > '9' and char <= 'O' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels