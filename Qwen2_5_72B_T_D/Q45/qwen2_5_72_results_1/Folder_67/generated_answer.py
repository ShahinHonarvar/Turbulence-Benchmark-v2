from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    letter_counts = Counter(substring)
    odd_count_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    even_length = len(substring) - len(odd_count_chars)

    def generate_palindromes(half, odd_chars, length):
        if length == 0:
            return {''}
        elif length == 1:
            return set(odd_chars)
        palindromes = set()
        for char in half:
            for middle in generate_palindromes(half.replace(char, '', 1), odd_chars, length - 2):
                palindromes.add(char + middle + char)
        return palindromes
    if len(odd_count_chars) < 2:
        possible_palindromes = generate_palindromes(''.join([char * (count // 2) for char, count in letter_counts.items()]), odd_count_chars, len(substring))
        return {palindrome for palindrome in possible_palindromes if len(palindrome) > 4}
    else:
        return set()