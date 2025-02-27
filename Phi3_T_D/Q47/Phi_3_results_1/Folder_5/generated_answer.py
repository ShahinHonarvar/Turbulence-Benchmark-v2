def palindromes_of_specific_lengths(input_string):
    start, end = (63, 70)
    substring = input_string[start:end + 1]
    filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for i in range(len(filtered_substring) - 3):
        for length in (4, 5):
            substr = filtered_substring[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes