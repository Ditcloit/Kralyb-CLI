import socket
import urllib.request
import psutil
import platform
import click

hostname = socket.gethostname()

external_ip = urllib.request.urlopen("https://ident.me").read().decode('utf8')

print("                   -`")
print("                  .o+`")
print("                 `ooo/")
print("                `+oooo:")
print("               `+oooooo:")
print("               -+oooooo+:")
print("             `/:-:++oooo+:")
print("            `/++++/+++++++:")
print("           `/++++++++++++++:")
print("          `/+++ooooooooooooo/`")
print("         ./ooosssso++osssssso+`")
print("        .oossssso-````/ossssss+`")
print("       -osssssso.      :ssssssso.")
print("      :osssssss/        osssso+++.")
print("     /ossssssss/        +ssssooo/-")
print("   `/ossssso+/:-        -:/+osssso+-")
print("  `+sso+:-`                 `.-/+oso:")
print(" `++:.                           `-/+/")
print("")
print("")
print("")
print("")
print(" ____  __.             .__         ___.    ")
print("|    |/ _|___________  |  | ___.__.\_ |__  ")
print("|      < \_  __ \__  \ |  |<   |  | | __ \ ")
print("|    |  \ |  | \// __ \|  |_\___  | | \_\ \\")
print("|____|__ \|__|  (____  /____/ ____| |___  /")
print("        \/           \/     \/          \/ CLI")
print("")
print("")
print("This program is free to use, so you can use it for commercial, personal or other uses, but its SALE AND HACKING USE IS PROHIBITED and if you agree with these conditions write (y) and if you don't (n).")
print("")
print("")




if click.confirm('Do you want to continue?', default=True):
    print("")
    print("")

    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]: 
            if bytes < factor:
                return f"{bytes:.2f} {unit} {suffix}"
            bytes /= factor



    print("{", "="*10, "System Information", "="*10, "}")
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"\n")
    print("\n")
    print("\n")

    print("{", "="*10, "CPU Information", "="*10, "}")
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU usage: {psutil.cpu_percent()}%")

    print("\n")
    print("\n")
    print("\n")



    print("{", "="*10, "RAM Information", "="*10, "}")
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Avaliable: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("{=====SWAP=====}")
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {get_size(swap.percent)}%")
    print("\n")
    print("\n")
    print("\n")

    print("{", "="*10, "Disk Information", "="*10, "}")
    print("Patitions and usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"/---- Device {partition.device} ----\\")
        print(f" MountPoint: {partition.mountpoint}")
        print(f" File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
                continue
        print(f"Total Size: {get_size(partition_usage.total)}")
        print(f"Used: {get_size(partition_usage.used)}")
        print(f"Free: {get_size(partition_usage.free)}")
        print(f"Percentage {partition_usage.percent}")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    print("\n")
    print("\n")
    print("\n")


    print("{", "="*10, "Network Information", "="*10, "}")
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"/==== Interface: {interface_name}====\\")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f" IP Address: {address.address}")
                print(f" NetMask: {address.netmask}")
                print(f" Broadcast IP: {address.netmask}")
            elif str(address.family) == 'AddressFamily.AF.PACKET':
                print(f" MAC Address: {address.address}")
                print(f" NetMask: {address.netmask}")
                print(f" Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    print("Local User: " + hostname)
    print("\n")
    print("\n")
    print("\n")



    print("Enter any text to exit the console.")
    input()









