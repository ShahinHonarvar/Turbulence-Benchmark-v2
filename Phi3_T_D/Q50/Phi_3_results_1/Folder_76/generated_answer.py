def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    def pair_count(word_list):
        seen = set()
        count = 0
        for word in word_list:
            word_sorted = ''.join(sorted(word.lower()))
            if word_sorted in seen:
                count += 1
            else:
                seen.add(word_sorted)
        return count
    filtered_list = [word for word in string_list if len(word) >= 3]
    return pair_count(filtered_list) >= 143