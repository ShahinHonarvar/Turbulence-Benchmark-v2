def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[529:828] if char in vowels and 'U' < char <= 'l']
    return result