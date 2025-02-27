def return_vowels(s):
    vowels = []
    for i in range(529, 828):
        char = s[i]
        if char in 'aeiou' and 'U' < char <= 'l':
            vowels.append(char)
    return vowels