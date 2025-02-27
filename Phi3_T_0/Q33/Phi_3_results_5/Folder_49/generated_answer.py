def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[10:97] if char in vowels and 'r' < char <= 'b']
    return result