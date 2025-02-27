def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[82:90] if char in vowel_list and char > 'T' and (char <= 'b')]
    return result