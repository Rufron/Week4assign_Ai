# Manual implementation (handles missing keys and types)
from functools import cmp_to_key

def _safe_compare(a, b):
    # helper to compare values robustly (None last)
    if a is None and b is None:
        return 0
    if a is None:
        return 1
    if b is None:
        return -1
    try:
        return (a > b) - (a < b)
    except TypeError:
        # fallback to string compare if types are incompatible
        return (str(a) > str(b)) - (str(a) < str(b))

def sort_dicts_by_key_manual(data, key, reverse=False):
    """
    Manual sort that:
    - Treats missing keys as None (pushed to end)
    - Handles mixed types safely by falling back to string comparison
    """
    def cmp_items(x, y):
        return _safe_compare(x.get(key, None), y.get(key, None))
    sorted_list = sorted(data, key=cmp_to_key(cmp_items), reverse=reverse)
    return sorted_list


if __name__ == "__main__":
    print("🟢 Script started...")

    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "Dave", "age": None},
    ]

    sorted_data = sort_dicts_by_key_manual(data, "age")
    print("✅ Sorted result:", sorted_data)
