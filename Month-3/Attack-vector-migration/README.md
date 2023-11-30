# Attack Vector Migration Documentation

## Overview

Attack vector migration involves the strategic redirection of potential threats, such as malicious attachments (.zip files in this case), away from the main production server to an isolated environment. This documentation outlines the process of attack vector migration through the implementation of mail manipulation techniques in the Tpot Honeypot.

Attack vector migration is implemented along with [Email manipulation](https://github.com/0hex7/IIPP-Internship/tree/main/Month-3/Email-manipulation).

## Background

The need for attack vector migration arises from the inherent risks associated with receiving emails containing potentially harmful attachments. In this scenario, the focus is on mitigating threats associated with .zip files. By leveraging mail manipulation techniques, we redirect emails with .zip attachments from the main production server to an isolated environment, thereby minimizing the risk of compromising critical systems.

## Mail Manipulation for Attack Vector Migration

### Implementation Steps

#### Mail Server and Procmail Setup

1. **Mail Server (Postfix) Installation:**
   - Install and configure the Postfix mail server.
   - Configure Postfix to work with Gmail relay.

2. **Domain Registration:**
   - Register a domain (e.g., nycuaiserver.ddns.net) on [www.noip.com](https://www.noip.com).
   
3. **Setting up DUC:**
   - Download and install DUC, associating the dynamic IP with the registered domain.

4. **MX Records Setup:**
   - Login to the domain registrar (no-ip) and add 1 MX record with the highest priority for the honeypot's hostname.

5. **Mail Server Test:**
   - Verify the mail server's functionality by sending a test email from a personal account to the mail server.

 **The mail server is set up, and incoming mails are being delivered.**

#### Procmail Setup

1. **Procmail Installation:**
   - Install Procmail on the system.

2. **Mail Forwarding Setup:**
   - Create rules in `~/.procmailrc` to forward emails with .zip attachments to a designated environment.
   - Modify the configuration file of the mail server (Postfix) to catch commands from Procmail.

## Isolated Environment Setup

1. **Isolated Accounts/ Servers:**
   - Add new users to the system.
   - Modify /etc/aliases to include these users.
   - Set up header checks in the Postfix configuration to reject emails not from the specified domain.

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

The integration of Postfix and Procmail facilitates attack vector migration by effectively redirecting emails with malicious .zip attachments to an isolated environment. This comprehensive approach significantly strengthens the security posture against .zip file-based threats, ensuring that the main production server remains protected from potential harm. The synergy between attack vector migration and mail manipulation creates a robust defense mechanism against a variety of adversarial tactics.
