from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(word):
        count = defaultdict(int)
        for letter in word:
            count[letter.lower()] += 1
        return frozenset(count.items())
    anagrams_count = 0
    seen = set()
    for string in strings:
        letter_counts = count_letters(string)
        if letter_counts not in seen:
            seen.add(letter_counts)
            duplicates = sum((1 for s in seen if count_letters(s) == letter_counts))
            if duplicates >= 2:
                anagrams_count += duplicates - 1
        elif letter_counts in seen:
            duplicates = sum((1 for s in seen if count_letters(s) == letter_counts))
            anagrams_count += duplicates - 1
    return anagrams_count <= 14