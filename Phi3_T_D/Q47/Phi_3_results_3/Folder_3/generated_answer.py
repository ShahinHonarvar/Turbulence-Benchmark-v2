from itertools import product

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for start_index in range(27, 96):
        for length in range(49, 52):
            if start_index + length <= 95:
                substring = text[start_index:start_index + length]
                if substring.isalpha():
                    mid_index = length // 2
                    first_half = substring[:mid_index]
                    second_half = substring[mid_index + 1:] if length % 2 else substring[mid_index:]
                    first_half_variations = [''.join(p) for p in product(*([letter.lower(), letter.upper()] for letter in first_half))]
                    second_half_variations = [''.join(p) for p in product(*([letter.lower(), letter.upper()] for letter in second_half))]
                    for first in first_half_variations:
                        for second in second_half_variations:
                            palindrome = first + second
                            if palindrome == palindrome[::-1]:
                                palindromes.add(palindrome)
    return palindromes