def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    result = [char for char in s[13:59] if char > 'D' and char <= 'v' and (char in vowels)]
    return result