from collections import Counter
    import itertools

def palindromes_between_indices(s):
    substring = s[6:10]
    counter = Counter(substring.lower())
    even_parts = {char: count // 2 for char, count in counter.items() if count > 1}
    odd_parts = {char: count for char, count in counter.items() if count % 2 == 1}

    def generate_palindromes(even_parts, odd_parts, length):
        half_palindrome = ''.join([char * even_parts[char] for char in even_parts])
        permutations = set([''.join(p) for p in itertools.permutations(half_palindrome)])
        palindromes = set()
        for half in permutations:
            if len(odd_parts) > 0:
                for odd in odd_parts:
                    full_palindrome = half + odd + half[::-1]
                    if len(full_palindrome) >= length:
                        palindromes.add(full_palindrome)
            else:
                full_palindrome = half + half[::-1]
                if len(full_palindrome) >= length:
                    palindromes.add(full_palindrome)
        return palindromes
    return generate_palindromes(even_parts, odd_parts, 5)