def return_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in input_str[46:49] if ch in vowels and '[' < ch <= 'p']
    return result