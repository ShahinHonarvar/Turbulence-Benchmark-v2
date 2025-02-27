def return_vowels(input_string):
    vowel_range_chars = [chr(x) for x in range(65, 71) if 'A' <= chr(x) <= 'G']
    return [char for char in input_string if char in 'AEIOU' and ord(char) >= ord(vowel_range_chars[0]) and (ord(char) <= ord(vowel_range_chars[-1]))]