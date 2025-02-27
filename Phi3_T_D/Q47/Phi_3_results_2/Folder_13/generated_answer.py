def palindromes_of_specific_lengths(text):
    start_index, end_index = (13, 95)
    length_range = range(57, 61)

    def is_palindrome(s):
        return s.upper() == s.upper()[::-1]
    palindromes = set()
    for i in range(start_index, end_index + 1):
        for j in length_range:
            if i + j - 1 <= end_index:
                candidate = text[i:i + j].strip().replace(' ', '')
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes