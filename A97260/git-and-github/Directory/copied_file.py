# Purpose: Verify disk space availability and report any issues.

import shutil
import sys

def has_sufficient_disk_space(disk_path, minimum_free_gigabytes, minimum_free_percent):
   """
   Checks if a specified disk has enough free space.

   Args:
       disk_path (str): The path to the disk to check.
       minimum_free_gigabytes (int): The required minimum free space in gigabytes.
       minimum_free_percent (int): The required minimum free space as a percentage.

   Returns:
       bool: True if there's sufficient space, False otherwise.
   """

   # Get disk usage statistics
   disk_usage = shutil.disk_usage(disk_path)

   # Calculate free space metrics
   free_percent = 100 * disk_usage.free / disk_usage.total  # Calculate percentage of free space
   free_gigabytes = disk_usage.free / 2**30  # Convert free space to gigabytes

   # Evaluate disk space against thresholds
   return (free_percent >= minimum_free_percent) and (free_gigabytes >= minimum_free_gigabytes)

# Check the root disk for at least 2 GB and 10% free space
if not has_sufficient_disk_space("/", 2, 10):
   print("Error: Insufficient disk space. Please ensure at least 2 GB and 10% of disk space is free.")
   sys.exit(1)  # Exit with an error code

print("Disk space is adequate.")
sys.exit(0)  # Exit successfully
