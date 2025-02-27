def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    word = text[2:6].lower()
    unique_chars = sorted(set(word))
    palindromes = set()
    for char_combination_length in range(3, len(unique_chars)):
        for combo in itertools.combinations(unique_chars, char_combination_length):
            middle = sorted(combo)
            if char_combination_length % 2 == 0:
                palindromes.add(''.join(middle + middle[::-1]))
            else:
                for mid_char in combo:
                    palindromes.add(''.join(middle + [mid_char] + middle[::-1]))
    return set(filter(is_palindrome, palindromes))