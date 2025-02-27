def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    result = [char for char in s[11:61] if char in vowels and char > 'M' and (char <= 'W')]
    return result