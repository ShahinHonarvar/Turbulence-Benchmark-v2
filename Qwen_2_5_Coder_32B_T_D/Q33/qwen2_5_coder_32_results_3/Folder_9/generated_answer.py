def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[13:35] if char > '8' and char <= 'F' and (char in vowels)]
    return result