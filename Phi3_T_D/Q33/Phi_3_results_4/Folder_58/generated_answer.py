def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[260:322] if char.lower() in vowels and char.lower() > '%' and (char.lower() <= 'u')]