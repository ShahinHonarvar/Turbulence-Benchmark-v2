def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in s[4:8] if char.lower() in vowels and 'p' < char.lower() <= 'r']
    return filtered_vowels