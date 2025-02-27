def return_vowels(input_str):
    vowels = {i: chr(i) for i in range(ord('E'), ord('H') + 1)}
    vowels.update({i: chr(i) for i in range(ord('a'), ord('e') + 1)})
    index_range_str = input_str[40:94]
    return [v for v in index_range_str if v in vowels]