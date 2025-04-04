import pytest

# def test_answer():
#     assert 5 == 2 + 3

class SimpleCache:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
            self.store[key] = value

    def get(self, key):
            return self.store.get(key, None)
        
@pytest.fixture
def cache():
    """"""
    test_cache = SimpleCache()
    yield test_cache # Test runs with this instance of SimpleCache

    # Teardown
    test_cache.store.clear()

def test_cache_set_and_get(cache):
    cache.set("test_key", "test_value")
    assert cache.get("test_key", "test_value") == "test_value", "Value should be retrievable after being set."

def test_cache_miss_returns_none(cache):
     assert cache.get("nonexistant_key") is None, "Cache miss should return None."





