from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:9].lower()
    counter = Counter(substring)
    single_chars = [char for char, count in counter.items() if count % 2 == 1]
    if len(single_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in counter.items()))
    palindromes = set()

    def generate_palindromes(half, single_char):
        if len(half) == 0:
            return
        if single_char:
            palindrome = half + single_char + half[::-1]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
        palindrome = half + half[::-1]
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    for i in range(len(half_palindrome) + 1):
        for single_char in ('', *single_chars):
            generate_palindromes(half_palindrome[:i], single_char)
    return palindromes