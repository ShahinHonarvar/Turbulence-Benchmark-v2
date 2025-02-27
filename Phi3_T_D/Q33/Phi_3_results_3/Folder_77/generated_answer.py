def return_vowels(input_string):
    vowels = [c for c in input_string[837:975] if 'N' < c <= 'W' and c in 'aeiouAEIOU']
    return vowels