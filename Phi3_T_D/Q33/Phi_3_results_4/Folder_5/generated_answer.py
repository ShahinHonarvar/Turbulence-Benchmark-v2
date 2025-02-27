def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[44:95] if char in vowel_list and char > 'f' and (char <= '<')]