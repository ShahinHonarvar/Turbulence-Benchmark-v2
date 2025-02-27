from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    letter_counts = Counter(substring)
    possible_palindromes = set()

    def generate_palindromes(partial, remaining):
        if len(partial) * 2 + sum((1 for count in remaining.values() if count > 0)) > 5:
            if all((remaining[letter] % 2 == 0 for letter in remaining)):
                half = partial + ''.join((letter * (remaining[letter] // 2) for letter in remaining))
                possible_palindromes.add(half + half[::-1])
        for letter in list(remaining):
            if remaining[letter] > 0:
                remaining[letter] -= 1
                generate_palindromes(partial + letter, remaining)
                remaining[letter] += 1
    generate_palindromes('', letter_counts)
    return possible_palindromes