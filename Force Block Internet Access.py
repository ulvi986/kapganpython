import subprocess

def block_internet_access():
    try:
        # Create a firewall rule to block all outbound connections
        subprocess.run(["netsh", "advfirewall", "firewall", "add", "rule",
                        "name=BlockInternet", "dir=out", "action=block"])

        print("Internet access blocked successfully.")
    except subprocess.CalledProcessError as e:
        print("Error blocking internet access:", e)

# Block internet access
block_internet_access()
