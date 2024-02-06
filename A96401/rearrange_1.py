import re

def rearrange_name(name):
    # Apply a regular expression to identify names in 'Last, First' format
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)

    # Validate the regular expression match
    if result is None:
        # Return the unmodified name if it doesn't conform to the expected pattern
        return name

    # Format the name into 'First Last' by swapping the matched groups
    return "{} {}".format(result[2], result[1])
