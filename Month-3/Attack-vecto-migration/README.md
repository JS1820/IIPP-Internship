# Attack Vector Migration Documentation

## Overview

Attack vector migration involves the strategic redirection of potential threats, such as malicious attachments (.zip files in this case), away from the main production server to an isolated environment. This documentation outlines the process of attack vector migration through the implementation of mail manipulation techniques in the Tpot Honeypot.

## Background

The need for attack vector migration arises from the inherent risks associated with receiving emails containing potentially harmful attachments. In this scenario, the focus is on mitigating threats associated with .zip files. By leveraging mail manipulation techniques, we redirect emails with .zip attachments from the main production server to an isolated environment, thereby minimizing the risk of compromising critical systems.

## Mail Manipulation for Attack Vector Migration

### Phase 1: Proposed Model

#### Model Overview

The proposed model in Phase 1 involves deploying a mail server within the honeypot and utilizing Suricata for monitoring email contents. Custom rules are developed to detect malicious .zip attachments, and suspicious emails are forwarded to another server for in-depth analysis.

![Screenshot 1](https://github.com/0hex7/IIPP-Internship/assets/108691415/faa8b926-8c03-4daf-bef8-14dd434e87d4)

#### Implementation Steps

1. **Mail Server Setup (Postfix):**
   - Install and configure the Postfix mail server.
   - Configure Postfix to work with Gmail relay.

2. **Suricata Integration:**
   - Develop custom Suricata rules to detect suspicious email activities, especially those related to .zip attachments.
   - Modify the Suricata container inside the Tpot honeypot to accommodate the custom rules.

3. **Issues and Alternatives:**
   - Acknowledge Suricata limitations and consider alternatives for functionalities like forwarding emails with .zip attachments.

### Phase 2: Alternative Approach

#### Introduction of Procmail

To address Suricata limitations, Procmail is introduced. Procmail is a versatile program for filtering, sorting, and storing emails. It plays a crucial role in the attack vector migration process.

#### Network Architecture

The network architecture includes hidden accounts/servers isolated from external threats.

![Screenshot 2023-11-30 115129](https://github.com/0hex7/IIPP-Internship/assets/108691415/23350eac-544f-4f71-9ff4-cbb114a03de9)

#### Isolated Accounts/ Servers

To isolate accounts:

- Add new users to the system.
- Modify /etc/aliases to include these users.
- Set up header checks in the Postfix configuration to reject emails not from the specified domain.

#### Procmail Setup

1. **Procmail Installation:**
   - Install Procmail on the system.

2. **Mail Forwarding Setup:**
   - Create rules in `~/.procmailrc` to forward emails with .zip attachments to a designated environment.
   - Modify the configuration file of the mail server (Postfix) to catch commands from Procmail.

## Emulation and Testing

The attack vector migration process is tested using various scenarios:

1. **Normal Mail to Admin:**
   - Send a normal mail to the admin account to ensure regular mail delivery.

   ![Screenshot 3](https://github.com/0hex7/IIPP-Internship/assets/108691415/925eaeab-9a9e-4478-adb7-510fad7226e3)

2. **.ZIP Mail to Admin:**
   - Send a mail with a .zip attachment to the admin account and observe the migration to the isolated environment.

   ![Screenshot 4](https://github.com/0hex7/IIPP-Internship/assets/108691415/14a46efe-d7f5-4441-90f7-4f6635185a7e)

3. **Phishing Mail to Admin:**
   - Send a phishing mail to the admin account and monitor the attack vector migration.

   ![Screenshot 5](https://github.com/0hex7/IIPP-Internship/assets/108691415/fdfbcebc-c864-473a-b73f-fe453a7c6552)

4. **.ZIP Mail to Tsec:**
   - Send a mail with a .zip attachment to the Tsec account and verify successful migration.

   ![Screenshot 6](https://github.com/0hex7/IIPP-Internship/assets/108691415/4d7671d0-17c1-4950-8bad-01e1c80b3340)

5. **Normal Mail to Tsec:**
   - Send a normal mail to the Tsec account to confirm that non-malicious emails are not affected.

   ![Screenshot 7](https://github.com/0hex7/IIPP-Internship/assets/108691415/c8cda0ce-5107-4470-b1d8-b9198b97d156)

## Conclusion

The integration of Postfix, Suricata, and Procmail facilitates attack vector migration by effectively redirecting emails with malicious .zip attachments to an isolated environment. This comprehensive approach significantly strengthens the security posture against .zip file-based threats, ensuring that the main production server remains protected from potential harm. The synergy between attack vector migration and mail manipulation creates a robust defense mechanism against a variety of adversarial tactics.
