def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    selected_vowels = [character for character in input_string[54:82] if character in vowels and character > '&' and (character <= '@')]
    return selected_vowels