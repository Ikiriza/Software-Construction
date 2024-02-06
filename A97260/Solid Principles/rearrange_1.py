import re

def format_name_last_first(name):
   """Rearranges a name from "First Name, Last Name" to "Last Name, First Name".

   Args:
       name (str): The name to rearrange.

   Returns:
       str: The rearranged name, or the original name if it doesn't match the expected format.
   """

   # Extract name parts using a regular expression
   match = re.search(r"^([\w .]*), ([\w .]*)$", name)

   # Check for a match
   if match:
       return "{} {}".format(match.group(2), match.group(1))  # Rearrange and return last name, first name

   return name  # Return original name if format doesn't match
