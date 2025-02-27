from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars, min_len):
        char_list = list(chars)
        palindromes = set()
        for perm in permutations(char_list, len(char_list)):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower() and len(candidate) >= min_len:
                palindromes.add(candidate)
        return palindromes
    substring = s[3:10]
    filtered_chars = ''.join(filter(str.isalpha, substring))
    if len(filtered_chars) < 3:
        return set()
    return generate_palindromes(filtered_chars, 3)