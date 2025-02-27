def return_vowels(input_string):
    vowels = 'aeiou'
    selected_vowels = [x for x in input_string[11:61] if x in vowels and 'M' < x <= 'W']
    return selected_vowels