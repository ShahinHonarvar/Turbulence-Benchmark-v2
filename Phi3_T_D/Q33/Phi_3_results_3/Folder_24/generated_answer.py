def return_vowels(s):
    vowels_list = []
    for char in s[23:57]:
        if 'a' <= char <= 'd' and char in 'aeiou':
            vowels_list.append(char)
    return vowels_list