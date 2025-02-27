def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_chars = [char for char in s[4:8] if 'q' < char <= 'r' and char in vowels]
    return filtered_chars