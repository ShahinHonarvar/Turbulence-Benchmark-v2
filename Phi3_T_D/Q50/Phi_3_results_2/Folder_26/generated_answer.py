def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_anagram(word, rest):
        norm_word = normalize(word)
        return any((normalize(an) == norm_word for an in rest))

    def count_anagrams(words):
        result = 0
        for i in range(len(words)):
            if has_anagram(words[i], words[i + 1:]):
                result += 1
        return result
    filtered_words = [w for w in lst if len(w) >= 3]
    return count_anagrams(filtered_words) >= 49