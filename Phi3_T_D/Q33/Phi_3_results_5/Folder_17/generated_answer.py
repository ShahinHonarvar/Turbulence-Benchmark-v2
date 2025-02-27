def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for char in s[60:99]:
        if char in vowels and 'j' < char <= 'n':
            result.append(char)
    return result