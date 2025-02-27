def palindromes_of_specific_lengths(s):
    s = s[10:56].lower()

    def find_palindromes(s, min_len, max_len):
        palindromes = set()
        for length in range(min_len, max_len + 1):
            for i in range(len(s) - length + 1):
                substr = s[i:i + length]
                if substr.isalpha() and substr == substr[::-1]:
                    palindromes.add(substr)
        return palindromes
    return find_palindromes(s, 3, 7)