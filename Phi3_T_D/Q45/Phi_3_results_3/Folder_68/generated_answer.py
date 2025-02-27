def palindromes_between_indices(s: str) -> set:
    start, end = (1, 8)
    chars = sorted(set(s[start:end].lower()))
    if len(chars) < 4:
        return set()

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def generate_palindromes(prefix: str, choices: list, n: int) -> set:
        if n == 0:
            yield prefix
        else:
            for c in choices:
                choice = [c] * n
                yield from generate_palindromes(prefix + c + prefix[::-1], choices, n - 2)
    palindromes = set()
    for i in range(4, len(chars) + 1, 2):
        if i % 2 == 0:
            choices = list({c: chars.count(c) for c in chars if chars.count(c) >= i // 2}.keys())
            if not choices:
                continue
            palindromes.update({p for p in generate_palindromes('', choices, i // 2)})
    return palindromes