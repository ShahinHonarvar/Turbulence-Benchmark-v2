def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[36:56] if char in vowels and '+' < char <= '/']
    return result