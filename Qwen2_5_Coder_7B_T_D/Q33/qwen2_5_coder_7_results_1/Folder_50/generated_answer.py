def return_vowels(s):
    vowels = [char for char in s[11:53] if char in 'aeiouAEIOU' and char > '+' and (char <= 'W')]
    return vowels