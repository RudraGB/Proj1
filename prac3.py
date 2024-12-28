#Question:
#Write a Python program that checks the disk usage of your system and alerts if the usage exceeds 80%.
#Requirements:
#Use the shutil module to fetch disk usage information.
#Display the total, used, and free space on the disk in gigabytes.
#If the disk usage percentage exceeds 80%, print an alert message.

import shutil

def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)

    total_gb= total / (2**30)
    used_gb = used /(2**30)
    free_space_gb = free / (2**30)
    

    print(f"Total:{total_gb}")
    print(f"Used:{used_gb}")
    print(f"free space:{free_space_gb}")
    
    disk_usage = used / total * 100
    if (disk_usage > 80):
        print("Warning: Disk usage exceeds 80%!")
    else:
        print("Disk usage is within safe limits.")

    get_disk_usage()


   