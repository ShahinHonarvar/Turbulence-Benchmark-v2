def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[23:57] if char in vowels and char > '0' and (char <= 'd')]
    return result