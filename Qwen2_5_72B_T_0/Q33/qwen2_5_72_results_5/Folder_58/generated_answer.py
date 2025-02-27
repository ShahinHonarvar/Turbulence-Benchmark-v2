def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[260:322] if char in vowels and char > '%' and (char <= 'U')]