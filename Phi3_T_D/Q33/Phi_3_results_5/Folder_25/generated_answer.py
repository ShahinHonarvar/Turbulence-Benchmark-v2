def return_vowels(input_string):
    vowels = set('aeiouAEIOU')
    return [char for char in input_string[28:76] if vowels.issuperset(char) and char > '+' and (char <= 'z')]