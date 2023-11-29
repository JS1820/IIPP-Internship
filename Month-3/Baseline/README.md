# Baseline Implementation in Tpot Honeypot

## Introduction

The baseline implementation within the Tpot Honeypot is a pivotal security measure, aiming to identify key system elements and establish a secure state that can be reverted to when needed. This process is critical for restoring an operational environment to a safe state and imposing a cost on adversaries by thwarting their activities.

### Scenario Overview

In a hypothetical scenario where an adversary gains access to the Tpot Honeypot and attempts to breach the main server, the baseline implementation becomes the frontline defense. Even if the honeypot is compromised, this strategy ensures a swift reset to a secure state, preventing unauthorized access and potential attacks on the primary environment.

## Tpot Honeypot Architecture

Tpot, an open-source honeypot framework, simplifies the deployment and management of honeypots for capturing and analyzing cyber threats. It integrates various honeypot containers (e.g., cowrie, adbhoneypot, conpot, ciscoasa, tanner, snare, heralding, etc.) that can be seamlessly deployed as Docker containers inside the Tpot environment.

### Default Ports and Issues

While the default port to connect to the Tpot web UI is `64294`, and the admin panel port is `64297`, these ports, integral for management, can also become potential targets for attackers. The baseline implementation actively addresses this vulnerability.

![Tpot Web UI and Admin Panel Ports](https://github.com/0hex7/IIPP-Internship/assets/108691415/bf4a5e4b-df6e-480b-b6ba-ab63db0e8e1f)

## Baseline Implementation Steps

### Step 1: Set Up the Honeypot

1. Deploy the Tpot Honeypot with all desired services running.
2. Verify the proper functioning of the honeypot.

### Step 2: Create a Baseline Snapshot

1. Shutdown the honeypot.
2. Create a snapshot using VMWare named "Tpotbaseline" to capture the secure state.
3. Ensure only essential services (e.g., Cowrie & Kibana) are running in this baseline.
![Screenshot 2023-11-06 000132](https://github.com/0hex7/IIPP-Internship/assets/108691415/a0edaf5e-8a0b-420f-858f-8ae221ee75b2)


### Step 3: Secure Configuration for Baseline

1. Define the baseline configuration with limited services running (Cowrie & Kibana).
2. Allow only the required ports to be open, such as ports `22`, `23`, and `64294`.
3. Set a complex password for enhanced security.

## Baseline Automation

To bolster security and responsiveness, the baseline implementation incorporates automation. The [Baseline-automation.py](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Baseline/Baseline-automation.py) script operates in the background, continuously monitoring the honeypot for unauthorized access.

![Baseline Automation Script](https://github.com/0hex7/IIPP-Internship/assets/108691415/2168d384-f1f0-4314-bab6-3d4df0e8beb3)

### Automation Steps

1. Generate a password list for brute-forcing the login page using [Password-generator.py](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Baseline/Password-generator.py).

![Password List Generation](https://github.com/0hex7/IIPP-Internship/assets/108691415/4f8bf019-caeb-48c6-879c-c5b3065c063e)

2. Encode the password for compliance with the authorization token header in HTTP requests.

   ![Password Encoding](https://github.com/0hex7/IIPP-Internship/assets/108691415/67702dd2-c8a6-412b-b37a-dda08a7c62f1)

3. Brute-force attack prevention: The script checks the web UI login page using the default username (`tsec`) and the current password. If the response is `200 OK`, indicating no unauthorized access, nothing happens. If the response differs, the script takes action.

4. Automated Response: In case of an unauthorized login attempt, the script stops the running Tpot honeypot and starts the baseline honeypot immediately.

## Benefits of Baseline Implementation

- Swift deployment of a secure baseline.
- Zero human interaction required for baseline activation.

![Baseline Activation](https://github.com/0hex7/IIPP-Internship/assets/108691415/c7694cc1-aed8-4106-88c5-4a3c0c9620bf)

- Continuous 24/7 monitoring for potential threats.
- Prevention of unauthorized access and potential malicious activities.

## Conclusion

![Baseline Implementation in Action](https://github.com/0hex7/IIPP-Internship/assets/108691415/14721deb-28e6-430e-a543-e3cfc01ddf81)

When an attacker changes the honeypot password, attempting to lock the defenders out, the baseline automatically deploys, safeguarding the environment.

![Baseline Automatic Deployment](https://github.com/0hex7/IIPP-Internship/assets/108691415/42b3d211-d59d-48c4-aead-2c622cc00412)

The successful implementation of the baseline in Tpot Honeypot, coupled with automation, significantly enhances the security posture of the environment. The baseline acts as a secure reset point, allowing the honeypot to revert quickly to a safe state when unauthorized access is detected. This proactive security measure prevents attackers from gaining control of critical systems and ensures a rapid response to potential threats.
