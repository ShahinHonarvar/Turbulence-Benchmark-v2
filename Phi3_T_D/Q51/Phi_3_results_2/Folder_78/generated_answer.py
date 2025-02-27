from collections import Counter

def if_contains_anagrams(strings):

    def counter_hash(s):
        return frozenset(Counter((c.lower() for c in s if c.isalpha())).items())
    counted_strings = {counter_hash(s): s for s in strings}
    unique_counts = {frozenset(Counter(s).items()): Counter(s.lower()) for s in counted_strings if len(s) >= 3}
    count_anagrams = 0
    for word, counter in unique_counts.items():
        if len(counter) == 2:
            for other in unique_counts:
                if word != other and set(word) == set(other):
                    count_anagrams += 1
                    if count_anagrams > 70:
                        return False
    return True