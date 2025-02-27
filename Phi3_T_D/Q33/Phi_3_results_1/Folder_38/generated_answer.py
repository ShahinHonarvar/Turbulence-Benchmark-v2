def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', '{']
    result = [char for char in string[17:65] if char in vowels and char > 'U' and (char <= '{')]
    return result