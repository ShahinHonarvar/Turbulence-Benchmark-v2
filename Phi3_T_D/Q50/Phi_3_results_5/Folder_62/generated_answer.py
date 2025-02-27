def if_contains_anagrams(lst):

    def count_sorted(s):
        return ''.join(sorted(s.lower()))

    def is_anagram_of_any(word, word_list):
        sorted_word = count_sorted(word)
        for other in word_list:
            if sorted_word == count_sorted(other) and word.lower() != other.lower():
                return True
        return False
    anagrams_count = 0
    seen_sorted = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = count_sorted(word)
            if sorted_word in seen_sorted:
                if is_anagram_of_any(word, seen_sorted[sorted_word]):
                    anagrams_count += 1
                seen_sorted[sorted_word].append(word)
            else:
                seen_sorted[sorted_word] = [word]
    return anagrams_count >= 43