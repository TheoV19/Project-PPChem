import re

def filter_cas(synonyms: list[str]):
    if synonyms is None:
        return None
    for s in synonyms:
        match = re.match(r"(\d{2,7}-\d\d-\d)", s)
        if match:
            return match.group(1)
    return None