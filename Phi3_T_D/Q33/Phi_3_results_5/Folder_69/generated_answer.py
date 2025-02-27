def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_chars_in_range = [char for char in input_string[641:872] if char in vowels and 'g' < char <= 'q']
    return vowel_chars_in_range