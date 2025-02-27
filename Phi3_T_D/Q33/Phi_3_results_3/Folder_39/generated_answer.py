def return_vowels(input_string):
    vowels = [chr(index) for index in range(98, 123) if chr(index) in ('a', 'e', 'i', 'o', 'u')]
    result = [char for char in input_string[31:96] if char in vowels and ord(char) > ord('q')]
    return result