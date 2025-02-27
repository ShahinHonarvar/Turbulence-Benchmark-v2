def palindromes_between_indices(s):
    letters = [ch.lower() for ch in s[6:9]]
    letter_count = {letter: letters.count(letter) for letter in set(letters)}

    def backtrack(path, remaining):
        letter = path.pop()
        palindrome = [letter.upper(), letter.lower()] + [letter.upper()] * (remaining // 2)
        if len(palindrome) >= 3:
            return [''.join(palindrome)]
        if letter in remaining:
            remaining = remaining.replace(letter, '', 1)
            return [p for subset in backtrack(path[:], remaining) for p in backtrack([letter] + path, remaining)]
        return []
    return set(backtrack(list((letter for _, count in letter_count.items() if count >= 1 for _ in range(count))), ''.join(letters)))