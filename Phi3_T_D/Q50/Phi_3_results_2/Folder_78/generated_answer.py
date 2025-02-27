from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    count = 0
    seen = defaultdict(int)
    for word in lst:
        for key in seen:
            if is_anagram(word, key):
                count += seen[key]
                seen[key] += 1
                break
        else:
            sorted_word = ''.join(sorted(word.lower()))
            words_count = seen[sorted_word]
            seen[sorted_word] = words_count + 1
            count += words_count
    return count >= 79