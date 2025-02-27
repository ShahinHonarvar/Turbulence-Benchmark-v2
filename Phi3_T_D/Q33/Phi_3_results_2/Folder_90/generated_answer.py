def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    characters = s[142:145]
    result = [char for char in characters if char > '4' and char <= 'o' and (char in vowels)]
    return result