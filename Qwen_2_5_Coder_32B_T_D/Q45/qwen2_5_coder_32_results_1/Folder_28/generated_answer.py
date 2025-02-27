from collections import Counter
    import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    relevant_chars = ''.join(filter(str.isalpha, s[1:6])).lower()
    char_count = Counter(relevant_chars)
    palindromes = set()
    for half_length in range(2, 3):
        for half in itertools.combinations_with_replacement(char_count.keys(), half_length):
            half_word = ''.join(half)
            if all((char_count[c] >= 2 * half_word.count(c) for c in set(half_word))):
                middle = ''
                if len(relevant_chars) % 2 == 1:
                    for char in char_count:
                        if char_count[char] % 2 == 1:
                            middle = char
                            break
                palindrome = half_word + middle + half_word[::-1]
                if is_palindrome(palindrome) and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes