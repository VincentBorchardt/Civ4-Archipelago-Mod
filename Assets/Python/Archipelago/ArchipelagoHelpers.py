# Helper Functions go here

def sanitizeCivText(szInput):
    """
    Escapes XML/HTML control characters so Civ 4's UI renderer doesn't truncate strings,
    and strips non-Latin1 characters that would render as broken boxes.
    """
    if not szInput:
        return ""

    # 1. Escape XML control characters so they render literally on screen
    szClean = szInput.replace("&", "&amp;")
    szClean = szClean.replace("<", "&lt;")
    szClean = szClean.replace(">", "&gt;")

    # 2. Strip any non-ASCII/Latin-1 characters (like emojis or Cyrillic) so they don't break Python 2.4
    try:
        szClean = szClean.encode("latin-1", "ignore")
    except Exception:
        # Fallback if the input is already a raw byte string
        szClean = "".join([c for c in szClean if ord(c) < 128])

    return szClean