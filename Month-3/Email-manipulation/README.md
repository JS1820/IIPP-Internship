# Implementing Email Manipulation in Tpot Honeypot

## Introduction

Implementing email manipulation in the Tpot Honeypot involves a two-phase approach. Phase 1 focuses on deploying a mail server, integrating Suricata for enhanced email security, and proposing a model for email manipulation. In Phase 2, an alternative approach is introduced to address Suricata limitations using Procmail.

## Phase 1: Proposed Model

### Model Overview

The proposed model in Phase 1 deploys a mail server within the honeypot, utilizing Suricata for monitoring email contents. Custom rules are developed to detect malicious attachments, and suspicious emails are forwarded to another server for in-depth analysis.

![Screenshot 1](https://github.com/0hex7/IIPP-Internship/assets/108691415/faa8b926-8c03-4daf-bef8-14dd434e87d4)

### Implementation Steps

#### Step 1: Mail Server Setup

In this setup, the [Postfix](https://github.com/vdukhovni/postfix) mail server is employed.

1. **Postfix Installation:**
   ```bash
   sudo apt install postfix
   ```

2. **Configuring Postfix for Gmail Relay:**
   Modify the configuration file (main.cf) to include the necessary lines. Refer to [Postfix-main.cf](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Postfix/Postfix-main.cf).

   ![Screenshot 1](https://github.com/0hex7/IIPP-Internship/assets/108691415/d059fec3-4043-4e37-9c87-c0e80de40a6f)
   ![Screenshot 2](https://github.com/0hex7/IIPP-Internship/assets/108691415/17372dc5-0f08-4577-ada2-d4ec4acded8f)
   ![Screenshot 3](https://github.com/0hex7/IIPP-Internship/assets/108691415/25c0ac9c-6f40-46c7-9352-ab64119a0f73)

   Note: This model can only send emails and cannot receive them due to the absence of a definitive domain name.

3. **Domain Registration:**
   Register a domain (e.g., nycuaiserver.ddns.net) on [www.noip.com](https://www.noip.com).

   ![Screenshot 4](https://github.com/0hex7/IIPP-Internship/assets/108691415/3f387633-c684-475b-bdee-64f871fecc1a)

4. **Setting up DUC:**
   Download and install DUC, associating the dynamic IP with the registered domain.

5. **MX Records Setup:**
   Log in to the domain registrar (no-ip) and add one MX record with the highest priority for the honeypot's hostname.

   ![Screenshot 5](https://github.com/0hex7/IIPP-Internship/assets/108691415/89cda257-be76-4a47-801e-85471c7f3ac4)
   ![Screenshot 6](https://github.com/0hex7/IIPP-Internship/assets/108691415/5e6d6325-f0b0-467b-85eb-3271c9b2beb0)

6. **Mail Server Test:**
   Verify the mail server's functionality by sending a test email from a personal account to the mail server.

   ![Screenshot 7](https://github.com/0hex7/IIPP-Internship/assets/108691415/6432d2fb-9daa-4bdb-a785-c07bc39aad3d)

**The mail server is set up, and incoming mails are being delivered.**

#### Step 2: Suricata Integration

1. **Suricata Rules:**
   Develop custom Suricata rules to detect suspicious email activities. Examples include alerting on SMTP logs for suspicious activity and detecting files found over SMTP.

   - Modify the prebuilt Suricata container inside the Tpot honeypot using the provided commands.

     ```bash
     docker exec -it suricata /bin/sh
     ```

     Inside the container, configure the rules and config files.

     ```bash
     apk add nano
     ```

     Remove the prebuilt config file.

     ```bash
     rm /etc/suricata/suricata.yaml
     ```

     Create a new file, copy the config file from [Suricata-suricata.yaml](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Suricata/Suricata-suricata.yaml), paste it into nano, and save it by pressing CTRL+x.

     ```bash
     nano /etc/suricata/suricata.yaml
     ```

     Create a local rules file and add the rules already built into the [Suricata rules](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Suricata/Suricata-local.rules) file.

     ```bash
     nano /var/lib/suricata/rules/local.rules
     ```

     Run Suricata with the updated config file and rules.

     ```bash
     suricata -c /etc/suricata/suricata.yaml -i eth0
     ```

2. **Issues and Alternatives:**
   Suricata has a few limitation with respect to forwarding mails if any SMTP rule is triggered. So, lets consider another approach to this..!

## Phase 2: Alternative Approach

### Suricata Limitations

Suricata has limitations in complex functionalities like forwarding emails, especially when triggered by specific rules. This leads to the introduction of an alternative approach in Phase 2.

### Introduction of Procmail

To address the limitations of Suricata, Procmail is introduced. Procmail is a program for filtering, sorting, and storing emails. It can be used both on mail clients and mail servers, making it a suitable tool for intricate email manipulation.

### Network Architecture

The network architecture includes hidden accounts/servers isolated from external threats.

![Screenshot 2023-11-30 115129](https://github.com/0hex7/IIPP-Internship/assets/108691415/23350eac-544f-4f71-9ff4-cbb114a03de9)

### Isolated Accounts/ Servers

To isolate accounts:

1. Add new users to the system.
2. Modify /etc/aliases to include these users.
3. Set up header checks in the Postfix configuration to reject emails not from the specified domain. Refer to [Postfix-main.cf](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Postfix/Postfix-main.cf).
   In this, there is a regex check for the headers.

   To implement header checks, follow these steps:

   ```bash
   sudo nano header_checks
   ```

   Copy-paste the rules from [Header_checks](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Postfix/Header_checks) file and save it using CTRL+X.

 
   Restart the Postfix mail server
   ```bash
   sudo systemctl restart postfix
   ```

   Once Postfix is restarted, it implements the isolation of two particular accounts i.e., `susmails` and `review-unit`.
   Any mail from an external mail server cannot reach these two accounts, but the internal mail server can reach them.

### Procmail Setup

[Procmail](https://github.com/Distrotech/procmail) can be used to create mail servers, mailing lists, sort your incoming mail into separate folders/files, preprocess your mail, and selectively forward certain incoming mail automatically to someone.

1. **Procmail Installation:**
   ```bash
   sudo apt install procmail
   ```

   All the forwarding recipes must be added to individual users from whose account we want to set up email forwarding if any rule is triggered.

2. **Mail Forwarding Setup:**
   - Create rules in `~/.procmailrc` to forward emails with .exe or .zip attachments to `reviewunit` and phishing emails to `susmails`. The rules are mentioned in [.procmailrc](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Email-manipulation/.procmailrc). Copy-paste them into your recipe file.

   ![Screenshot 2](https://github.com/0hex7/IIPP-Internship/assets/108691415/10129e4d-ea40-400b-ac36-941680604e96)

   - Create a `procmail.log` file in the home directory using the command `touch procmail.log`.
   - Now, modify the configuration file of the mail server i.e., Postfix to catch commands from Procmail.

     ```bash
     sudo rm /etc/postfix/main.cf
     ```

     Copy-paste the contents of [Postfix-main.cf](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Postfix/Postfix-main.cf) file into nano, and save it using CTRL+x.

     ```bash
     nano /etc/postfix/main.cf
     ```

     Restart the Postfix mail server.

     ```bash
     systemctl restart postfix
     ```

Now everything is set up; let's perform some test emulations and observe the results!

## Emulation and Testing

### Normal Mail to Admin

Send a normal mail to the admin account.

![Screenshot 3](https://github.com/0hex7/IIPP-Internship/assets/108691415/925eaeab-9a9e-4478-adb7-510fad7226e3)

### .ZIP Mail to Admin

Send a mail with a .zip attachment to the admin account.

![Screenshot 4](https://github.com/0hex7/IIPP-Internship/assets/108691415/14a46efe-d7f5-4441-90f7-4f6635185a7e)

### Phishing Mail to Admin

Send a phishing mail to the admin account.

![Screenshot 5](https://github.com/0hex7/IIPP-Internship/assets/108691415/fdfbcebc-c864-473a-b73f-fe453a7c6552)

### .ZIP Mail to Tsec

Send a mail with a .zip attachment to the Tsec account.

![Screenshot 6](https://github.com/0hex7/IIPP-Internship/assets/108691415/4d7671d0-17c1-4950-8bad-01e1c80b3340)

### Normal Mail to Tsec

Send a normal mail to the Tsec account.

![Screenshot 7](https://github.com/0hex7/IIPP-Internship/assets/108691415/c8cda0ce-5107-4470-b1d8-b9198b97d156)

## Conclusion

The integration of Postfix, Suricata, and Procmail enhances the honeypot's defenses against adversarial email attacks. Custom rules and filtering mechanisms enable the detection and isolation of suspicious emails, providing an automated and robust system for email manipulation and analysis. This approach significantly strengthens the security posture against various attack vectors.
