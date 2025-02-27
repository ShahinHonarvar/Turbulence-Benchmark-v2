def palindromes_of_specific_lengths(input_string):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    for length in range(23, 39):
        for start in range(41, 90 - length + 2):
            potential_palindrome = input_string[start:start + length]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes