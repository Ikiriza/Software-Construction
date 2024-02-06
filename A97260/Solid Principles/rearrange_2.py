import re

def format_name_last_first(name):
   """Rearranges a name from "First Name, Last Name" to "Last Name, First Name".

   Args:
       name (str): The name to rearrange.

   Returns:
       str: The rearranged name, or the original name if it doesn't match the expected format.
   """

   # Extract name parts using a regular expression that includes hyphens
   match = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

   # Check for a matching name format
   if match:
       # Rearrange the name components
       formatted_name = f"{match.group(2)} {match.group(1)}"
       return formatted_name  # Return last name, first name

   # If the format doesn't match, return the original name
   return name
