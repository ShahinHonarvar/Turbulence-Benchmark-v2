def palindromes_of_specific_lengths(text):

    def find_palindromes(s, min_len, max_len):
        palindromes = set()
        for length in range(min_len, max_len + 1):
            for start in range(len(s) - length + 1):
                substring = s[start:start + length]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
        return palindromes
    return find_palindromes(text[21:63], 22, 33)