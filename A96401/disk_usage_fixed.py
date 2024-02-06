import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """
    Verifies that the disk has sufficient free space.

    Parameters:
        - disk (str): Path to the disk to be checked.
        - min_absolute (int): Minimum required free space in bytes.
        - min_percent (int): Minimum required free space as a percentage of total disk space.

    Returns:
        - bool: Returns True if the disk meets the free space criteria, False otherwise.
    """
    # Retrieve disk usage statistics for the specified path
    disk_stats = shutil.disk_usage(disk)

    # Compute free space as a percentage of total space
    free_space_percent = 100 * disk_stats.free / disk_stats.total

    # Convert free space to gigabytes for comparison
    free_space_gb = disk_stats.free / (2**30)

    # Determine if free space falls below either threshold
    if free_space_percent < min_percent or free_space_gb < min_absolute:
        # Insufficient free space detected
        return False

    # Sufficient free space available
    return True

# Perform disk space check for root ("/") with thresholds of 2 GB absolute and 10% relative free space
if not check_disk_usage("/", 2*2**30, 10):
    # Notify if disk space is below required thresholds
    print("ERROR: Insufficient disk space available")
    # Indicate an error condition with a non-zero exit code
    return(1)

# Confirm sufficient disk space availability
print("Disk space check passed")
# Indicate success with a zero exit code
return(0)
