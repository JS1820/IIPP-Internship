# Baseline Implementation in Tpot Honeypot

## Introduction

The baseline implementation in Tpot Honeypot is crucial for identifying key system elements and establishing a secure state to revert to when necessary. Reverting to a baseline configuration is essential for restoring an operational environment to a safe state or imposing a cost on adversaries by preventing their activity.

### Scenario Overview

Consider a scenario where an adversary gains access to the Tpot Honeypot and attempts to access the main server. The implementation of a baseline ensures that, even if compromised, the honeypot can be reset to a secure state, preventing unauthorized access and potential attacks on the main environment.

## Tpot Honeypot Architecture

Tpot is an open-source honeypot framework designed to simplify the deployment and management of honeypots for capturing and analyzing cyber threats. It includes various honeypot containers (e.g., cowrie, adbhoneypot, conpot, ciscoasa, tanner, snare, heralding, etc.) that can be deployed as Docker containers inside the Tpot environment.

### Default Ports and Issues

The default port to connect to the web UI of Tpot is `64294`, and the default port for the admin panel is `64297`. While these ports are necessary for management, they can become potential targets for attackers. The implementation of a baseline addresses this issue.

## Baseline Implementation Steps

### Step 1: Set Up the Honeypot

- Deploy the Tpot Honeypot with all the desired services running.
- Verify the proper functioning of the honeypot.

### Step 2: Create a Baseline Snapshot

- Shutdown the honeypot.
- Create a snapshot using VMWare named "Tpotbaseline" to capture the secure state.
- Ensure that only essential services (e.g., Cowrie & Kibana) are running in this baseline.

### Step 3: Secure Configuration for Baseline

- Define the baseline configuration with limited services running (Cowrie & Kibana).
- Allow only the required ports to be open, such as ports `22`, `23`, and `64294`.
- Set a complex password for enhanced security.

## Baseline Automation

To enhance the security and responsiveness of the baseline implementation, automation is introduced. The [Baseline-automation.py](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Baseline/Baseline-automation.py) script is designed to run in the background and monitor the honeypot for any unauthorized access.

### Automation Steps

1. Encode the password: The script encodes the password to comply with the authorization token header in HTTP requests.
2. Brute-force attack prevention: The script sends a request to the web UI login page with the default username (`tsec`) and the current password. If the response is `200 OK`, indicating no unauthorized access, nothing happens. If the response is different, the script takes action.
3. Automated Response: If an unauthorized login attempt is detected, the script stops the currently running Tpot honeypot and starts the baseline honeypot immediately.

## Benefits of Baseline Implementation

- Quick deployment of a secure baseline.
- No human interaction required for baseline activation.
- Continuous monitoring 24/7 for potential threats.
- Prevents unauthorized access and potential malicious activities.

## Conclusion

The successful implementation of the baseline in Tpot Honeypot, along with automation, enhances the security posture of the environment. The baseline serves as a secure state to which the honeypot can be reverted when unauthorized access is detected. This proactive security measure helps prevent attackers from gaining control of critical systems and ensures a rapid response to potential threats.
