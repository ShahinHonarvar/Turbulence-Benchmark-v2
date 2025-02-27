def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_range = input_string[23:75]
    return [char for char in selected_range if char.lower() in vowels and 'l' < char.lower() <= 'd']