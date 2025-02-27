def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return [char for char in string[90:97] if char > '_' and char <= 'x' and (char in vowels)]