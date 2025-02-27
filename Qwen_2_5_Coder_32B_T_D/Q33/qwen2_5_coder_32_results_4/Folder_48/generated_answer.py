def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[529:828] if vowels.count(char) and 'U' < char <= 'l']