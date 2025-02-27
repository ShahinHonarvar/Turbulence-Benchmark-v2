def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:10].lower()
    unique_chars = set(substring)
    char_count = {char: substring.count(char) for char in unique_chars}
    palindromes = set()
    for length in range(3, 7):
        for chars in itertools.combinations_with_replacement(unique_chars, length // 2):
            left_half = ''.join(chars)
            right_half = left_half[::-1]
            middle = ''.join([char for char, count in char_count.items() if count % 2 != 0])
            candidate = left_half + middle + right_half
            if is_palindrome(candidate) and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes