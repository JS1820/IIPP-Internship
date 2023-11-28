# Honeypot Implementation - Phase 1


## Overview

Honeypots are decoy servers designed to attract attackers and monitor their activities to enhance intrusion detection and threat response. This documentation focuses on the implementation of the HonSSH tool and network manipulation setup.

## Honeypot Concepts

### Types of Honeypots

1. **Pure Honeypot:**
   - Completely mimics the production system, resource-intensive.
   
2. **High-interaction Honeypot:**
   - Designed to get attackers to invest as much time as possible inside the honeypot.

3. **Mid-interaction Honeypot:**
   - Imitates elements of the application layer but lacks an operating system.

4. **Low-interaction Honeypot:**
   - Less resource-intensive, lacks content to hold the attacker’s attention for a considerable time.

### Techniques Used in Honeypots

#### Deception Techniques

1. **Port and Service Deception:**
   - Simulating open ports and services to attract attackers.

2. **Data Deception:**
   - Providing fake data or files that seem valuable to attackers.

3. **Credential Deception:**
   - Presenting fake login screens to capture attacker credentials.

4. **Protocol Deception:**
   - Simulating network protocols and behaviors that may not exist in the real environment.

## HonSSH

[HonSSH](https://github.com/tnich/honssh) is designed for use with a high interaction honeypot, sitting between an attacker and a honeypot, creating two separate SSH connections.

### Features

- Captures all connection attempts to a text file, database, or email alerts.
- Automatically replaces incorrect password attempts with the correct password (spoof_login option).
- Captures a text-based summary of an attacker's session.
- Real-time session viewing or hijacking through the management telnet interface.
- Downloads copies of files transferred through wget or scp.
- Uses Docker to spin up new honeypots and reuse them based on IP.
- Advanced networking features to spoof attackers' IP addresses between HonSSH and the honeypot.

### Installation

1. Git clone the HonSSH repository: [HonSSH GitHub Repo](https://github.com/tnich/honssh).
2. Edit the `honssh.cfg.default` file with suitable values.
3. Navigate to the directory and run HonSSH.

#### Installation Error

- If an error occurs during installation, it needs to be rectified before proceeding.

### Network Manipulation Setup

- **VM1 (Attacker):** Kali Linux
- **VM2 (Gateway):** Ubuntu Server
- **VM3 (Analysis & Logging):** Ubuntu Server 18.0 with Elasticsearch, Kibana, Logstash.
- **CT1 (Frontend Decoy):** Ubuntu LCX
- **CT2 (Backend Decoy):** Ubuntu LCX with MySQL, Apache, etc.

#### Additional Setup

- **CT1 (Frontend Decoy):** Ubuntu LCX, serving as a fake frontend, tunneled via SSH.
- **CT2 (Backend Decoy):** Ubuntu LCX, serving as a decoy backend, tunnels data via SSH.

### Next Steps in Implementation

1. Rectify the error in HonSSH.
2. Set up ELK (Elasticsearch, Logstash, Kibana) in VM3.
3. Configure SSH tunneling in Frontend and Backend Decoys.
4. Configure VM1 Kali Linux.
5. Set up fake virtual IPs in the network via HonSSH.
6. Implement the password logging feature of HonSSH.
7. Integrate and test the final environment using real-world attack scenarios.

## References

- [Research Paper on the Combination of Deceptive Network and Honeypots](https://iaeme.com/MasterAdmin/Journal_uploads/IJEET/VOLUME_12_ISSUE_6/IJEET_12_06_027.pdf)

&nbsp;
&nbsp;
&nbsp;
&nbsp;

&nbsp;
&nbsp;


I had to stop using HonSSH because of a few issues with the network setup, i had in my mind, So i had to find an alternative Honeypot.!
# Honeypot Implementation - Phase 2

## Tpot CE - Overview

[Tpot CE (Community Edition)](https://github.com/telekom-security/tpotce) is an all-in-one honeypot platform developed by Telekom-Security. It supports multiple honeypots and visualization options using the Elastic Stack. This phase focuses on Tpot CE and associated honeypots.

### Tpot CE - Honeypots Included

1. **Cowrie Honeypot Features:**
   - Fake file system
   - SSH Monitor
   - Saves Downloaded file using wget & curl
   - Can be configured to run as a Hive

2. **Conpot Honeypot Features:**
   - Can mimic industrial control systems (ICS)
   - Event Logging
   - Alerts and Notifications
   - Passive Monitoring

3. **Endlessh Honeypot Features:**
   - Idle Interaction
   - Minimal Resource Usage
   - No Logging mechanism
   - Limited Interaction

4. **Dionaea Honeypot Features:**
   - Emulates SSH, FTP, HTTP
   - Captures Malwares
   - Low Interaction honeypot

### ELK Stack Features

- **Elastic Search + Logstash + Kibana:**
   - Great Visualization modes
   - Can be integrated with IDS and SIEM
   - Logging Mechanism

### Tools Included

- **Cockpit:**
   - Detailed View
   - Live Attack view
   - Manage Logs

- **Fatt (Packet Analyser):**
   - Uses Tshark/Wireshark
   - Network Fingerprinting

- **P0f:**
   - Purely passive traffic fingerprinting.

- **Spiderfoot:**
   - Open source intelligence automation tool.

- **Suricata:**
   - Network Security Monitoring engine.

### Technical Architecture Of Tpot
![image](https://github.com/0hex7/IIPP-Internship/assets/108691415/6af33860-552a-4368-a07a-17ffc3f700dc)

#### System Setup

- VMWare VM running on Windows with,
- 12 Gb RAM
- 150 Gb SSD
- Bridged Network with a Static IP: 140.113.110.151

I also used another VM instance to run it in local network with NAT configuration with IP: 192.168.98.135

#### Installation Steps

1. Download ISO Image from [Debian Netboot](http://ftp.debian.org/debian/dists/bullseye/main/installer-amd64/current/images/netboot/mini.iso) or,
2. Git Clone the Repository:
   ```bash
   git clone https://github.com/telekom-security/tpotce
   cd tpotce
## Post-Installation Steps

Once installed on the VM machine, follow these steps:

1. **Login:**
   - Use `tsec` as the username and the setup password (During the Installation, we are supposed to input a password for the Default user: Tsec).

2. **Successful Login:**
   - Access the Web-Based Login Interface using the same credentials.

3. **Access Terminal using Web UI:**
   - Access all Services.
   - Access the Logs.
   - Access Overall Health: `<IP>:64294`


