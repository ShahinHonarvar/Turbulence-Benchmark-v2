def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[51:77] if '4' < char <= '=' and char in vowels]
    return result