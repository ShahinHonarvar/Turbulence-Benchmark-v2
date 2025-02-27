def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for char in s[23:38]:
        if char in vowels and 'N' < char <= 'k':
            result.append(char)
    return result