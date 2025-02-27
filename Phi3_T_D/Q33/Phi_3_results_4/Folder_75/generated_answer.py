def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    selected_vowels = [char for char in input_string[20:41] if char > 'K' and char <= 'Z' and (char in vowels)]
    return selected_vowels