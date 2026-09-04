def count_items(items):
    # TODO: use a for loop to build a dictionary counting each item in `items`
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts