
def prefix_func(s):
    """Computes prefix function of the pattern."""

    n = len(s)
    pi = [0] * n  # stores lengths of longest prefix for each position
    j = 0         # current length of the prefix match

    for i in range(1, n):
        # if mismatch -> fallback
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        # if match -> extend the current prefix
        if s[i] == s[j]:
            j += 1

        pi[i] = j

    return pi


def longest_proper_prefix(s):
    """Returns the longest proper prefix of a string that is also its suffix."""

    pi = prefix_func(s)
    length = pi[-1] 

    if length == 0:
        return ""
    else:
        return s[:length]

print(longest_proper_prefix("baobab"))   # must return b
print(longest_proper_prefix("azazaz"))  # must return azaz
print(longest_proper_prefix("qwerty"))    # must return empty string ""
