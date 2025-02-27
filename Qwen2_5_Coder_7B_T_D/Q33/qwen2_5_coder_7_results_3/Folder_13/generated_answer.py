def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[149:313] if char in vowels and 'M' < char <= 'j']
    return result