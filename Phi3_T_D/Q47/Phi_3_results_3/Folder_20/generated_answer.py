def palindromes_of_specific_lengths(text):
    prefix = text[20:75]
    candidate_substrings = {prefix[i:j] for i in range(len(prefix)) for j in range(i + 36, min(i + 43, len(prefix)) + 1)}
    candidate_substrings = {substring.lower() for substring in candidate_substrings if substring.isalpha()}
    palindromes = {substring for substring in candidate_substrings if substring == substring[::-1]}
    return palindromes