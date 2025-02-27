def return_vowels(s):
    vowels = []
    for i in range(10, 97):
        char = s[i]
        if char in 'aeiou' and 'R' < char <= 'b':
            vowels.append(char)
    return vowels