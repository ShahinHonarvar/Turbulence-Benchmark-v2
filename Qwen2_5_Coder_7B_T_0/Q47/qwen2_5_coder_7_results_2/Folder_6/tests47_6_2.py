from Q47.qwen2_5_coder_7_results_2.Folder_6.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(98, 47)
    m = min(98 - 45 + 1, 47)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(40, m + 1)}


def test_string_of_similar_nums():
    n = max(98, 47)
    m = min(98 - 45 - 1, 47)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (98 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (98 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (98 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(98 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 40 <= len(i) <= 47


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(98 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[45: 98 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (98 * 3)
    assert not palindromes_of_specific_lengths(s)
    