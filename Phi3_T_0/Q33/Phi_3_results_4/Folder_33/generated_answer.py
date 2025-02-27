def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[163:771] if char in vowels and char > ':' and (char <= 'E')]