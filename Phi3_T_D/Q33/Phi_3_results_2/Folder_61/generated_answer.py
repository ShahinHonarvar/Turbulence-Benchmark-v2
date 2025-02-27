def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    specified_vowels = vowels[vowels.index('c') + 1:vowels.index('i') + 1]
    return [char for char in s[1:4] if char in specified_vowels]