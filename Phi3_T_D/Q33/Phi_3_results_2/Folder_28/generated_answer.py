def return_vowels(string):
    vowel_list = []
    for char in string[41:50]:
        if 'E' <= char <= ']':
            if char in 'AEIOUaeiou':
                vowel_list.append(char)
    return vowel_list