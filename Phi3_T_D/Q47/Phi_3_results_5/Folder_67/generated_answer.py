def palindromes_of_specific_lengths(s: str) -> set:
    """
    Find palindromes of lengths between 26 to 33 in the substring from index 65 to index 99.
    Only consider English letters, case-insensitive.

    :param s: Input string
    :return: Set of valid palindromes
    """
    substring = s[65:100]
    valid_palindromes = set()
    for l in range(26, 34):
        for start_index in range(26 - l + 1):
            end_index = start_index + l
            if substring[start_index:end_index].isalpha():
                potential_palindrome = substring[start_index:end_index]
                if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                    valid_palindromes.add(potential_palindrome)
    return valid_palindromes