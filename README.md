# Network Automation with Python & Netmiko

## Project Overview
This project automates the configuration of a **2-Tier Network Architecture** (Access & Distribution layers). It utilizes Python and the `Netmiko` library to configure VLANs across multiple Cisco IOS switches simultaneously.

## Topology
![Network Topology](topology.png)
*Designed using GNS3 with Cisco IOSvL2 images.*

## Features
* **Scalable:** Uses loops and dictionaries to manage multiple devices.
* **Layer-Separated Logic:** Applies different configurations based on switch roles (Access vs. Aggregation).
* **Automated Verification:** Connects via SSH and saves configurations (`write memory`).

## Tools Used
* **Language:** Python 3
* **Libraries:** Netmiko
* **Environment:** Linux Mint, GNS3, VS Code

## How to Run
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the script:
    ```bash
    python network_config.py
    ```

## Output Proof
!![Script Execution](assets/execution_proof.png)