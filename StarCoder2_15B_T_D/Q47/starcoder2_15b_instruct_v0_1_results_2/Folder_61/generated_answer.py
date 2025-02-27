def palindromes_of_specific_lengths(s: str) -> set:
    """
    Finds all palindromes of specific lengths in a given string.
    """
    substring = s[0:31]
    result = set()
    for length in range(20, 31):
        start_index = 0
        while start_index + length - 1 < len(substring):
            is_palindrome = True
            for i in range(length // 2):
                if substring[start_index + i].lower() != substring[start_index + length - 1 - i].lower():
                    is_palindrome = False
                    break
            if is_palindrome:
                result.add(substring[start_index:start_index + length])
                start_index += length
            else:
                start_index += 1
    return result