def palindromes_of_specific_lengths(input_string):

    def is_english_letter(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    def extract_palindromes(s, start, end, min_length, max_length):
        palindromes = set()
        for length in range(min_length, max_length + 1):
            for i in range(start, end - length + 1):
                substring = s[i:i + length]
                if substring == substring[::-1] and all((is_english_letter(c) for c in substring)):
                    palindromes.add(substring.lower())
        return palindromes
    return extract_palindromes(input_string, 0, 5, 3, 5)