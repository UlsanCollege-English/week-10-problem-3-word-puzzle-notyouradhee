"""
HW03 — Group anagrams using a dictionary.
No type hints. Standard library only.
"""
def _clean_letters(s):
    """Return lowercase letters from s (a-z)."""
    return ''.join(ch.lower() for ch in s if ch.isalpha())

def _signature(s):
    """Return sorted lowercase-letter signature for s."""
    return ''.join(sorted(_clean_letters(s)))

def group_anagrams(words):
    """Return dict: signature -> list of original words in input order."""
    d = {}
    for w in words:
        key = _signature(w)
        if key not in d:
            d[key] = []
        d[key].append(w)
    return d

if __name__ == "__main__":
    pass
