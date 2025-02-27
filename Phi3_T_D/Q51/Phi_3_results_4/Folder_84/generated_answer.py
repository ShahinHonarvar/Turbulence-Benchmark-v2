from collections import Counter

def if_contains_anagrams(strings):

    def count_letters(s: str) -> Counter:
        return Counter(s.lower())
    anagram_pairs = 0
    seen = {}
    for s in strings:
        if len(s) < 3:
            continue
        letter_count = count_letters(s)
        for key in seen:
            if letter_count == seen[key]:
                if anagram_pairs + 1 > 16:
                    return False
                anagram_pairs += 1
                break
        else:
            seen[count_letters(s)] = seen.get(count_letters(s), 0) + 1
    return True