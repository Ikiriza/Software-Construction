import shutil

def has_sufficient_disk_space(disk, min_free_bytes, min_free_percent):
   """Determines whether a specified disk has enough free space.

   Args:
       disk (str): The disk path to check.
       min_free_bytes (int): The minimum free space required in bytes.
       min_free_percent (int): The minimum free space required as a percentage.

   Returns:
       bool: True if there's sufficient space, False otherwise.
   """

   # Retrieve disk usage statistics
   disk_usage = shutil.disk_usage(disk)  # Get disk usage information

   # Calculate free space metrics
   free_percent = 100 * disk_usage.free / disk_usage.total  # Calculate percentage of free space
   free_gigabytes = disk_usage.free / 2**30  # Convert free space to gigabytes

   # Evaluate free space against thresholds
   if free_percent < min_free_percent or free_gigabytes < min_free_bytes:
       return False  # Insufficient space

   return True  # Sufficient space

# Check the root disk for at least 2 GB and 10% free space
if not has_sufficient_disk_space("/", 2 * 2**30, 10):
   print("Error: Insufficient disk space.")
   exit(1)  # Exit with error code 1

print("Disk space is adequate.")
exit(0)  # Exit with success code 0
