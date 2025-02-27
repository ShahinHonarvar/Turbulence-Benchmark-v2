def return_vowels(s):
    vowels = []
    if 8 < len(s):
        for char in s[8:9]:
            if 'Y' < char <= 's' and char in 'aeiou':
                vowels.append(char)
    return vowels