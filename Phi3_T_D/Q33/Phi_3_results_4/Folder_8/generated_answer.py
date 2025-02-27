from string import ascii_lowercase

def return_vowels(input_string):
    vowel_index_range = range(64, 83)
    vowels = set('aeiou')
    result = [char for index, char in enumerate(input_string) if char in vowels and index in vowel_index_range and (char > 'p') and (char <= 'z')]
    return result