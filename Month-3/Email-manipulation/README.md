Certainly! Below is the GitHub-flavored Markdown version of the documentation:


# Implementing Email Manipulation in Tpot Honeypot - Detailed Documentation



## 1. Introduction<a name="introduction"></a>

The implementation of email manipulation in Tpot Honeypot involves two phases. Phase 1 focuses on the proposed model, deploying a mail server and integrating Suricata for enhanced email security. Phase 2 introduces an alternative approach, addressing Suricata limitations through the use of Procmail.

## 2. Phase 1: Proposed Model<a name="phase-1-proposed-model"></a>

### Model Overview<a name="model-overview"></a>

The proposed model in Phase 1 involves deploying a mail server in the honeypot and utilizing Suricata for monitoring email contents. Custom rules are developed to detect malicious attachments, and suspicious emails are forwarded to another server for in-depth analysis.

### Implementation Steps<a name="implementation-steps"></a>

#### Step 1: Mail Server Setup<a name="step-1-mail-server-setup"></a>

1. **Postfix Installation:**
   ```bash
   sudo apt install postfix
   ```

2. **Configuring Postfix:**
   Modify the configuration file and add [link to postfix GitHub repo](https://github.com).

3. **Domain Registration:**
   Register a domain (e.g., nycuaiserver.ddns.net) on [www.noip.com](https://www.noip.com).

4. **Setting up DUC:**
   Download and install DUC, associating the dynamic IP with the registered domain.

5. **MX Records Setup:**
   Login to the domain register (no-ip) and add 1 MX record with the highest priority for the honeypot's hostname.

6. **Mail Server Test:**
   Verify the mail server's functionality by sending a test email to a personal account.

7. **Drawback and Solution:**
   The mail server can't receive emails due to the absence of a definitive domain name. The solution is to buy a domain name and set up MX records to point to the required hostname.

   ![Screenshot 1](https://github.com/0hex7/IIPP-Internship/assets/108691415/faa8b926-8c03-4daf-bef8-14dd434e87d4)

#### Step 2: Suricata Integration<a name="step-2-suricata-integration"></a>

1. **Suricata Rules:**
   Develop custom Suricata rules to detect suspicious email activities. Examples include alerting on SMTP logs for suspicious activity and detecting files found over SMTP.

2. **Issues and Alternatives:**
   Suricata limitations are acknowledged, and alternatives are considered for functionalities like forwarding emails with .exe attachments.

## 3. Phase 2: Alternative Approach<a name="phase-2-alternative-approach"></a>

### Suricata Limitations<a name="suricata-limitations"></a>

Suricata has limitations in complex functionalities like forwarding emails, especially when triggered by specific rules. This leads to the introduction of an alternative approach in Phase 2.

### Introduction of Procmail<a name="introduction-of-procmail"></a>

To address the limitations of Suricata, Procmail is introduced. Procmail is a program for filtering, sorting, and storing emails. It can be used both on mail clients and mail servers, making it a suitable tool for intricate email manipulation.

### Network Architecture<a name="network-architecture"></a>

The network architecture includes hidden accounts/servers isolated from external threats.

### Isolated Accounts/ Servers<a name="isolated-accounts-servers"></a>

To isolate accounts:
- Add new users to the system.
- Modify /etc/aliases to include these users.
- Set up header checks in the Postfix configuration to reject emails not from the specified domain.

### Procmail Setup<a name="procmail-setup"></a>

1. **Procmail Installation:**
   ```bash
   sudo apt install procmail
   ```

2. **Mail Forwarding Setup:**
   Create rules in `~/.procmailrc` to forward emails with .exe or .zip attachments to `reviewunit` and phishing emails to `susmails`.

   ![Screenshot 2](https://github.com/0hex7/IIPP-Internship/assets/108691415/10129e4d-ea40-400b-ac36-941680604e96)

## 4. Emulation and Testing<a name="emulation-and-testing"></a>

### Normal Mail to Admin<a name="normal-mail-to-admin"></a>
Send a normal mail to the admin account.

![Screenshot 3](https://github.com/0hex7/IIPP-Internship/assets/108691415/925eaeab-9a9e-4478-adb7-510fad7226e3)

### .ZIP Mail to Admin<a name="zip-mail-to-admin"></a>
Send a mail with a .zip attachment to the admin account.

![Screenshot 4](https://github.com/0hex7/IIPP-Internship/assets/108691415/14a46efe-d7f5-4441-90f7-4f6635185a7e)

### Phishing Mail to Admin<a name="phishing-mail-to-admin"></a>
Send a phishing mail to the admin account.

![Screenshot 5](https://github.com/0hex7/IIPP-Internship/assets/108691415/fdfbcebc-c864-473a-b73f-fe453a7c6552)

### .ZIP Mail to Tsec<a name="zip-mail-to-tsec"></a>
Send a mail with a .zip attachment to the tsec account.

![Screenshot 6](https://github.com/0hex7/IIPP-Internship/assets/108691415/4d7671d0-17c1-4950-8bad-01e1c80b3340)

### Normal Mail to Tsec<a name="normal-mail-to-tsec"></a>
Send a normal mail to the tsec account.

![Screenshot 7](https://github.com/0hex7/IIPP-Internship/assets/108691415/c8cda0ce-5107-4470-b1d8-b9198b97d156

)

## 5. Conclusion<a name="conclusion"></a>

The integration of Postfix, Suricata, and Procmail enhances the honeypot's defenses against adversarial email attacks. Custom rules and filtering mechanisms enable the detection and isolation of suspicious emails, providing an automated and robust system for email manipulation and analysis. This approach significantly strengthens the security posture against various attack vectors.
```

Please note that the images are linked from the provided URLs, so they should be accessible when viewing the documentation on GitHub. Make sure to replace the image URLs with the actual URLs where your images are hosted.
