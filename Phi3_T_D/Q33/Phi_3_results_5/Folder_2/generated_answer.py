def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    ascii_E = ord('E')
    ascii_tilde = ord('~')
    result = []
    for char in string[170:645]:
        if char in vowels and ascii_E < ord(char) <= ascii_tilde:
            result.append(char)
    return result