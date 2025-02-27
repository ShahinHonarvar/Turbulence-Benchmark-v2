def palindromes_of_specific_lengths(input_string):
    substring = input_string[15:95]
    valid_palindromes = set()

    def is_english_letter(char):
        return 'A' <= char <= 'Z' or 'a' <= char <= 'z'
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and all((is_english_letter(c) for c in candidate)):
                valid_palindromes.add(candidate)
    return valid_palindromes