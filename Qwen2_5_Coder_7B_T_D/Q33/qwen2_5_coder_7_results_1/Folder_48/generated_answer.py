def return_vowels(s):
    return [char for char in s[529:828] if char in 'aeiou' and char > 'U' and (char <= 'l')]