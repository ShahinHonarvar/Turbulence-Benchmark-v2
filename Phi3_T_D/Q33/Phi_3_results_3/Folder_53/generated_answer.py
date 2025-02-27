def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    target_range = s[27:57]
    filtered_vowels = [char for char in target_range if char > 'o' and char <= 'w' and (char in vowels)]
    return filtered_vowels