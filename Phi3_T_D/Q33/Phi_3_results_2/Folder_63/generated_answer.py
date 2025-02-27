def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[34:69] if char in vowels and 'falls' < char <= 'o']
    return result