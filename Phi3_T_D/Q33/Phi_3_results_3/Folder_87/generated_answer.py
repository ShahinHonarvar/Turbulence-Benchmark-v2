def return_vowels(s):
    start, end = (34, 58)
    vowels = []
    for index in range(start, end):
        char = s[index]
        if 'a' < char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels