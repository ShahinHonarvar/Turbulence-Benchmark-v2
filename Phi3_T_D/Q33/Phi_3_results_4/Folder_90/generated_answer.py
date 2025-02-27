def return_vowels(input_string):
    vowels = [c for c in input_string[142:145] if 'a' <= c <= 'o' and c in 'aeiou']
    return vowels