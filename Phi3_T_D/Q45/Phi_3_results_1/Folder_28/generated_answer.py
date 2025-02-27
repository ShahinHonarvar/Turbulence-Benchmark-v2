from itertools import permutations

def palindromes_between_indices(text):
    substring = text[1:6].lower()
    letter_count = {}
    for char in substring:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    def can_form_palindrome(counts):
        odd_counts = [v % 2 for v in counts.values()]
        return sum(odd_counts) <= 1

    def build_palindromes(chars):
        for p in set(permutations(chars)):
            half = p[:len(p) // 2]
            candidate = ''.join(half) + ''.join(half[::-1])
            if candidate[len(candidate) // 2] in letter_count and candidate[:len(candidate) // 2].count(candidate[len(candidate) // 2]) < letter_count[candidate[len(candidate) // 2]]:
                if len(candidate) >= 4 and can_form_palindrome(dict(zip(chars, [half.count(c) for c in set(half)]))):
                    yield candidate
    return set(build_palindromes(letter_count.keys()))