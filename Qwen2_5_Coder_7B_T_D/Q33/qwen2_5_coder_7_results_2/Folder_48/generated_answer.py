def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[529:828] if char in vowels and char > 'U' and (char <= 'l')]
    return result