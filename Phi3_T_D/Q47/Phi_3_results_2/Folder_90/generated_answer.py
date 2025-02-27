def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(data):
    start_idx = 106
    end_idx = 280
    min_length = 136
    max_length = 151
    substring = data[start_idx:end_idx + 1]
    valid_sub = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(len(valid_sub) - length + 1):
            candidate = valid_sub[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes