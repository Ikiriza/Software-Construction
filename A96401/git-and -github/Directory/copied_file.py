# Copied this script into a new location using: cp ../disk_usage_fixed.py copied_file.py
# Then prepared it for version control with: git add copied_file.py
import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """
    Checks disk space availability. Returns True for adequate space, False for insufficient.
    """
    # Retrieve disk usage stats
    disk_stats = shutil.disk_usage(disk)
    # Determine free space percentage
    free_space_percent = 100 * disk_stats.free / disk_stats.total
    # Compute free space in gigabytes
    free_gigabytes = disk_stats.free / 2**30
    # Assess if space meets minimum requirements
    if free_space_percent < min_percent or free_gigabytes < min_absolute:
        return False  # Not enough space based on criteria
    return True  # Sufficient space available

# Validate disk space against requirements: 2 GB and 10% minimum
if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")  # Alert on insufficient disk space
    sys.exit(1)  # Exit with error status

print("Disk space is sufficient")  # Confirm adequate disk space
sys.exit(0)  # Exit successfully
