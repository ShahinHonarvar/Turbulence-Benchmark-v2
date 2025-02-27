def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i, char in enumerate(string):
        if i >= 51 and i < 77 and (char > '4') and (char <= '=') and (char in vowels):
            result += char
    return result