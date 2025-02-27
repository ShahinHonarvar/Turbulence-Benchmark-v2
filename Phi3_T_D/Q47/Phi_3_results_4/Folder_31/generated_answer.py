def find_all_substring_palindromes(s, start, end, min_length, max_length):
    palindromes = set()
    for i in range(start, end + 1):
        for length in range(min_length, max_length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and len(substring) == length and (substring == substring[::-1]):
                palindromes.add(substring.lower())
    return palindromes

def palindromes_of_specific_lengths(s):
    return find_all_substring_palindromes(s, 10, 82, 37, 60)