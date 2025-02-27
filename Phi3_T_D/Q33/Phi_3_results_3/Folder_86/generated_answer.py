def return_vowels(text):
    vowels = 'aeiou'
    desired_range = text[273:275]
    filtered_vowels = [char for char in desired_range if char in vowels and char > '+' and (char <= 'o')]
    return filtered_vowels