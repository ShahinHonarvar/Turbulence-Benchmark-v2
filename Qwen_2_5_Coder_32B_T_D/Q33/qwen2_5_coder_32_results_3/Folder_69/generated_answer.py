def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[641:872] if 'a' < char <= 'q' and char in vowels]