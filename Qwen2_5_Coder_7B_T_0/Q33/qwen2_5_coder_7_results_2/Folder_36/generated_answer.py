def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[604:949] if char in vowels and 'N' < char <= 'U']
    return result