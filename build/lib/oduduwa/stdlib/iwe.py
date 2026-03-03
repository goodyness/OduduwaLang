def ka(oruko_iwe):
    """Read the full content of a file (ka iwe)."""
    with open(oruko_iwe, 'r', encoding='utf-8') as f:
        return f.read()

def ko(oruko_iwe, nkan):
    """Write text to a file, overwriting existing (ko sinu iwe)."""
    with open(oruko_iwe, 'w', encoding='utf-8') as f:
        f.write(str(nkan))

def fi_kun(oruko_iwe, nkan):
    """Append text to a file (fikun iwe)."""
    with open(oruko_iwe, 'a', encoding='utf-8') as f:
        f.write(str(nkan))
