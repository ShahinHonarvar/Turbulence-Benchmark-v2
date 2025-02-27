def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    target_vowels = [char for char in s[74:96] if char.lower() in vowels and 'j' < char.lower() <= 'x']
    return target_vowels