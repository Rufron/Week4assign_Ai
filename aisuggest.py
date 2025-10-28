def sort_dicts_by_key_ai(data, key, reverse=False):
    """
    Sort a list of dictionaries by a given key.
    Handles missing keys and None values gracefully.
    """
    def safe_value(d):
        v = d.get(key, None)
        if v is None:
            return (1, '')  # missing values go last
        return (0, v)
    return sorted(data, key=safe_value, reverse=reverse)


if __name__ == "__main__":
    print("🤖 AI Suggest Script Started...")

    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob"},
        {"name": "Charlie", "age": 25},
        {"name": "Dave", "age": None},
    ]

    sorted_data = sort_dicts_by_key_ai(data, "age")
    print("✅ Sorted Result:", sorted_data)
