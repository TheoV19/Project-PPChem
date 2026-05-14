#type:ignore
from organomind.cas import filter_cas

def test_filter_cas_found():
    synonyms = ["aspirin", "50-78-2", "2-acetyloxybenzoic acid"]
    assert filter_cas(synonyms) == "50-78-2"

def test_filter_cas_not_found():
    synonyms = ["aspirin", "no cas here"]
    assert filter_cas(synonyms) is None

def test_filter_cas_none():
    assert filter_cas(None) is None

def test_filter_cas_empty():
    assert filter_cas([]) is None