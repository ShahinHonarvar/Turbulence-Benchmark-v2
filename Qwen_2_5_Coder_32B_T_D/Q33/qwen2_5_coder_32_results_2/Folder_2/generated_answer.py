def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'O', 'U']
    return [char for char in s[170:645] if char in vowels and char > 'E' and (char <= '~')]