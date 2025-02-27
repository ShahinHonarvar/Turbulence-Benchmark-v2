def return_vowels(s):
    vowels = []
    for char in s[63:79]:
        if char in 'aeiouAEIOU' and 'D' < char <= 'y':
            vowels.append(char)
    return vowels