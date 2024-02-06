import re

def rearrange_name(name):
    # Apply regex to find names in 'Last, First' format, allowing for spaces, periods, and hyphens
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

    # Verify the regex found a match indicating the expected name format
    if result == None:
        # Return unchanged name if it doesn't fit the 'Last, First' pattern
        return name

    # If matched, reformat the name to 'First Last' using captured groups
    return "{} {}".format(result[2], result[1])
