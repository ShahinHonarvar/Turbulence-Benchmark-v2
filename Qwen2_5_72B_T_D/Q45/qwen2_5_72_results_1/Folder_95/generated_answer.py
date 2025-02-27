from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(letters, min_length):
        unique_letters = set(letters.lower())
        palindromes = set()
        for permutation in permutations(unique_letters, len(unique_letters)):
            for i in range(len(permutation)):
                for j in range(i + 1, len(permutation) + 1):
                    candidate = permutation[i:j]
                    if len(candidate) >= min_length and candidate == candidate[::-1]:
                        palindromes.add(''.join(candidate))
        return palindromes
    substring = s[7:9]
    letters = [char for char in substring if char.isalpha()]
    return generate_palindromes(letters, 3)