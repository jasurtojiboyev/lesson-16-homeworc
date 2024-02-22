def str(input_string):
    capital_indices = []
    for index, char in enumerate(input_string):
        if char.isupper():
            capital_indices.append(index)
    return capital_indices

# Example usage:

print(str("eDaBiT"))

