def remove_duplicates(items):
    # TODO: use a loop to build a new list with duplicates removed, keeping first occurrences
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items