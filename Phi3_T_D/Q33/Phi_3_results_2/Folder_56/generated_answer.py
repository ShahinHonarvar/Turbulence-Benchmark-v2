def return_vowels(s):
    return [char for char in s[15:86] if char > '@' and char <= '~' and (char in 'aeiouAEIOU')]