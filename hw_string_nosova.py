
def longest_proper_prefix(word):
    """Returns the longest proper prefix of a string that is also its suffix."""

    n = len(word)
    prefix = [0] * n   # stores lengths of longest prefix-suffix for each position
    j = 0              # current length of the prefix-suffix match

    for i in range(1, n):
        # if mismatch -> fallback
        while j > 0 and word[i] != word[j]:
            j = prefix[j - 1]

        # if match -> extend the current prefix-suffix
        if word[i] == word[j]:
            j += 1

        # store the length of the current match
        prefix[i] = j

    length = prefix[-1]

    # returns prefix as a string (or empty string "" if none)
    return word[:length]

print(longest_proper_prefix("baobab"))   # must return b
print(longest_proper_prefix("azazaz"))  # must return azaz
print(longest_proper_prefix("qwerty"))    # must return empty string ""
