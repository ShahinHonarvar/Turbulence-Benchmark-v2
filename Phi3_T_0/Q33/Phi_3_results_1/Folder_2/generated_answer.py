def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[170:645] if char in vowels and 'e' < char <= '~']