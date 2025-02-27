from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    counter = Counter(substring)
    middle_chars = ''
    possible_palindromes = set()
    for char, count in counter.items():
        if count % 2 != 0:
            middle_chars += char
        possible_palindromes |= {char * (count // 2)}
    if len(middle_chars) > 1:
        middle_chars = middle_chars[0]
    if len(possible_palindromes) == 0:
        return set()
    for _ in range(3):
        new_palindromes = set()
        for palindrome in possible_palindromes:
            for char, count in counter.items():
                if count >= 2 and palindrome.count(char) < count // 2:
                    new_palindromes.add(palindrome + char)
        possible_palindromes |= new_palindromes
    final_palindromes = set((palindrome + middle_chars + palindrome[::-1] for palindrome in possible_palindromes))
    return {palindrome for palindrome in final_palindromes if len(palindrome) >= 6}