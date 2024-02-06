import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """
    Evaluates available disk space to ensure it meets specified criteria.

    Parameters:
    - disk (str): Path of the disk to evaluate.
    - min_absolute (int): Minimum required free space in bytes.
    - min_percent (int): Minimum required free space as a percentage of total disk space.

    Returns:
    - bool: Returns True if the available space meets or exceeds requirements, False otherwise.
    """
    # Retrieve current disk usage details
    usage_stats = shutil.disk_usage(disk)

    # Determine free space as a percentage
    free_space_percentage = 100 * usage_stats.free / usage_stats.total

    # Convert free space to gigabytes for comparison
    free_space_in_gb = usage_stats.free / 2**30

    # Verify against both absolute and percentage thresholds
    if free_space_percentage < min_percent or free_space_in_gb < min_absolute:
        return False  # Not enough free space based on given criteria

    return True  # Sufficient free space available

# Verify root ("/") disk has at least 2 GB and 10% free
if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: Insufficient disk space")
    # Signal an error due to insufficient disk space
return(1)  # Use exit(1) for an error condition in script context

print("Disk space is adequate")
# Signal successful check with no issues
return(0)  # Use exit(0) for successful completion in script context
