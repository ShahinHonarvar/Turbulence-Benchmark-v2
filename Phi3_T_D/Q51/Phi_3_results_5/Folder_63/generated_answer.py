def if_contains_anagrams(strings):

    def count_anagrams(sub_list):
        sorted_sub_list = [''.join(sorted(s.lower())) for s in sub_list if len(s) >= 3]
        seen = set()
        anagram_count = 0
        for item in sorted_sub_list:
            if item in seen:
                anagram_count += 1
                if anagram_count > 423:
                    return True
            else:
                seen.add(item)
        return False
    pairs = [(strings[i], strings[j]) for i in range(len(strings)) for j in range(i + 1, len(strings))]
    return count_anagrams(pairs)