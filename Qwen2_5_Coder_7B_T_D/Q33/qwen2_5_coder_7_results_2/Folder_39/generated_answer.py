def return_vowels(s):
    vowels = []
    for i in range(32, 97):
        char = chr(i)
        if char in 'eiouy' and 'Q' < char <= ']':
            vowels.append(char)
    return vowels