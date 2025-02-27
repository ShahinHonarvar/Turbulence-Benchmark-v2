def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[13:35] if vowels > char > '8' and char <= 'F']
    return result