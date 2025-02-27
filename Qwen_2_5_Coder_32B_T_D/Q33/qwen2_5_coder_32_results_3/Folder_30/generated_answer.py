def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in s[11:61] if char > 'M' and char <= 'W' and (char in vowels)]
    return result