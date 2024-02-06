import shutil

def has_enough_disk_space(disk, min_free_gb=2, min_free_percent=10):
    """
    Checks if a disk has enough free space.

    Args:
        disk (str): The path to the disk to check.
        min_free_gb (int, optional): The minimum required free space in gigabytes. Defaults to 2.
        min_free_percent (int, optional): The minimum required free space as a percentage of the total disk space. Defaults to 10.

    Returns:
        bool: True if there is enough free space, False otherwise.
    """

    du = shutil.disk_usage(disk)
    free_percent = 100 * du.free / du.total
    free_gb = du.free / 2**30

    if free_percent < min_free_percent or free_gb < min_free_gb:
        return False

    return True

# Check for at least 2 GB and 10% free space on the root disk
if not has_enough_disk_space("/"):
    print("ERROR: Insufficient disk space available on root disk.")
    return 1

print("Sufficient disk space available.")
return 0
