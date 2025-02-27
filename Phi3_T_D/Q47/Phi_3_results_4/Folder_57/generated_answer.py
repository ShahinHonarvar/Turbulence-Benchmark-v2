def palindromes_of_specific_lengths(input_string):
    subset = input_string[15:95].lower()

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes(string):
        palindromes = set()
        for length in range(39, 53):
            for i in range(len(string) - length + 1):
                candidate = string[i:i + length]
                if all((c.isalpha() for c in candidate)) and is_palindrome(candidate):
                    palindromes.add(candidate)
        return palindromes
    return get_palindromes(subset)