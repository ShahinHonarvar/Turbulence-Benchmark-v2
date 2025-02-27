def return_vowels(s):
    result = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in s[19:20]:
        if char > 'm' and char <= 'p' and (char in vowels):
            result.append(char)
    return result