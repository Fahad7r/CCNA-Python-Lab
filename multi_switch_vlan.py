# 1. Import necessary modules
from netmiko import ConnectHandler

# 2. Define device dictionaries with specific configurations
# Using a data-driven approach where commands are embedded in the device dict
switches = [
    # --- Access Layer Switches ---
    # Switch 1: HR Department
    {
        "device_type": "cisco_ios",
        "host": "192.168.122.10",
        "username": "admin",
        "password": "cisco",
        "cmds": ["vlan 10", "name HR"],
    },
    # Switch 2: Development Department
    {
        "device_type": "cisco_ios",
        "host": "192.168.122.11",
        "username": "admin",
        "password": "cisco",
        "cmds": ["vlan 20", "name Development"],
    },
    # Switch 3: Mixed Departments (Dev & Sales)
    {
        "device_type": "cisco_ios",
        "host": "192.168.122.12",
        "username": "admin",
        "password": "cisco",
        "cmds": ["vlan 20", "name Development", "vlan 30", "name Sales"],
    },
    # --- Aggregation / Distribution Layer Switches ---
    # Dist Switch 1: All VLANs
    {
        "device_type": "cisco_ios",
        "host": "192.168.122.13",
        "username": "admin",
        "password": "cisco",
        "cmds": ["vlan 10", "name HR", "vlan 20", "name Development", "vlan 30", "name Sales"],
    },
    # Dist Switch 2: All VLANs
    {
        "device_type": "cisco_ios",
        "host": "192.168.122.14",
        "username": "admin",
        "password": "cisco",
        "cmds": ["vlan 10", "name HR", "vlan 20", "name Development", "vlan 30", "name Sales"],
    },
]

# 3. Define global commands (Save Configuration)
save_commands = ["exit", "do write"]

# 4. Start the automation process
print("Starting Network Automation...")

for device in switches:
    # Extract specific commands for the current device
    # .pop() removes the key from the dictionary so Netmiko doesn't get confused
    config_commands = device.pop("cmds")

    try:
        # 5. Establish SSH Connection
        print(f"\nConnecting to IP: {device['host']}... ⏳")
        connection = ConnectHandler(**device)
        print("Success! Login Successful")

        # 6. Send configuration set (Specific cmds + Save cmds)
        print("Applying configurations...")
        output = connection.send_config_set(config_commands + save_commands)

        # 7. Print the output to console for verification
        print("-" * 80)
        print(output)
        print("-" * 80)

        # 8. Close the connection
        connection.disconnect()
        print(f"Finished configuring {device['host']} successfully.")

    except Exception as e:
        # Error Handling: Print error and continue to the next device
        print(f"Login failed for IP: {device['host']}")
        print(f"Error details: {e}")
        print("Moving to next device...")

print("Mission Complete. All devices processed.")