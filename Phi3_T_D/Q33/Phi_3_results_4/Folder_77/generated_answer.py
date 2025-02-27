def return_vowels(input_string):
    result = [char for char in input_string[837:975] if char in vowels and char > 'N' and (char <= 'W')]
    return result