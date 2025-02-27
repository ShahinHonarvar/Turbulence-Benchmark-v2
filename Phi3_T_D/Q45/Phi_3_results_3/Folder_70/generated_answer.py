from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:7].lower()
    counts = {letter: letters.count(letter) for letter in set(letters)}
    half_len = sum((min(2, v) for v in counts.values())) // 2

    def create_half_palindrome(half_letters):
        palindrome_half = []
        pairs = [[k] * v for k, v in half_letters.items() if v > 1]
        singletons = [k for k, v in half_letters.items() if v == 1]
        for L in permutations(pairs):
            for pair_perm in permutations(L):
                for comb in range(len(pair_perm) + 1):
                    palindrome_half.append(''.join(pair_perm[:comb]) + ''.join(singletons) + ''.join(pair_perm[comb:][::-1]))
        return palindrome_half
    palindromes = set()
    for half_len in range(half_len, -1, -1):
        for comb in create_half_palindrome({k: count - 2 for k, count in counts.items() if count > 1}):
            if len(comb) >= 4:
                other_half = comb + comb[-2::-1] if palindromes else comb[-2::-1]
                palindromes.add(other_half + comb)
    palindromes = {p.upper() for p in palindromes if len(p) >= 4}
    return palindromes