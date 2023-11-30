
# Implementing Email Manipulation in Tpot Honeypot 



## 1. Introduction<a name="introduction"></a>

The implementation of email manipulation in Tpot Honeypot involves two phases. Phase 1 focuses on the proposed model, deploying a mail server and integrating Suricata for enhanced email security. Phase 2 introduces an alternative approach, addressing Suricata limitations through the use of Procmail.

## 2. Phase 1: Proposed Model<a name="phase-1-proposed-model"></a>

### Model Overview<a name="model-overview"></a>

The proposed model in Phase 1 involves deploying a mail server in the honeypot and utilizing Suricata for monitoring email contents. Custom rules are developed to detect malicious attachments, and suspicious emails are forwarded to another server for in-depth analysis.

 ![Screenshot 1](https://github.com/0hex7/IIPP-Internship/assets/108691415/faa8b926-8c03-4daf-bef8-14dd434e87d4)

 

### Implementation Steps<a name="implementation-steps"></a>

#### Step 1: Mail Server Setup<a name="step-1-mail-server-setup"></a>
We are using [postfix](https://github.com/vdukhovni/postfix) mail server in this setup.

1. **Postfix Installation:**
   ```bash
   sudo apt install postfix
   ```

2. **Configuring Postfix to work with Gmail relay:**
   Modify the configuration file(main.cf) to add the following lines
   ![Screenshot 2023-11-15 025842](https://github.com/0hex7/IIPP-Internship/assets/108691415/d059fec3-4043-4e37-9c87-c0e80de40a6f)
   ![Screenshot 2023-11-30 112739](https://github.com/0hex7/IIPP-Internship/assets/108691415/17372dc5-0f08-4577-ada2-d4ec4acded8f)
   ![Screenshot 2023-11-30 112827](https://github.com/0hex7/IIPP-Internship/assets/108691415/25c0ac9c-6f40-46c7-9352-ab64119a0f73)

A drawback of this model, is that we can only send the mails, we can not receive any mails, because we haven't setup any doamin name for our IP address.

3. **Domain Registration:**
   Register a domain (e.g., nycuaiserver.ddns.net) on [www.noip.com](https://www.noip.com).
   ![Screenshot 2023-11-30 113044](https://github.com/0hex7/IIPP-Internship/assets/108691415/3f387633-c684-475b-bdee-64f871fecc1a)

4. **Setting up DUC:**
   Download and install DUC, associating the dynamic IP with the registered domain.

5. **MX Records Setup:**
   Login to the domain register (no-ip) and add 1 MX record with the highest priority for the honeypot's hostname.
   
   ![Screenshot 2023-11-30 113140](https://github.com/0hex7/IIPP-Internship/assets/108691415/89cda257-be76-4a47-801e-85471c7f3ac4)

   ![Screenshot 2023-11-30 113418](https://github.com/0hex7/IIPP-Internship/assets/108691415/5e6d6325-f0b0-467b-85eb-3271c9b2beb0)
   

6. **Mail Server Test:**
   Verify the mail server's functionality by sending a test email to a personal account.

   ![Screenshot 2023-11-30 113514](https://github.com/0hex7/IIPP-Internship/assets/108691415/6432d2fb-9daa-4bdb-a785-c07bc39aad3d)
   

7. **Drawback and Solution:**
   The mail server can't receive emails due to the absence of a definitive domain name. The solution is to buy a domain name and set up MX records to point to the required hostname.

  

#### Step 2: Suricata Integration<a name="step-2-suricata-integration"></a>

1. **Suricata Rules:**
   Develop custom Suricata rules to detect suspicious email activities. Examples include alerting on SMTP logs for suspicious activity and detecting files found over SMTP.
   First we need to modify the prebuilt suricata container inside tpot honeypot by executing following commands in order.
   docker exec -it suricata /bin/sh --> we are inside the container, we can now configure the rules and config files
   apk add nano  --> to add nano
   rm /etc/suricata/suricata.yaml --> remove the prebuilt config file
   nano /etc/suricata/suricata.yaml --> create a new file and copy the config file from [Suricata-suricata.yaml](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Suricata/Suricata-suricata.yaml) and paste it into nano, and save it by doing CTRL+x
   nano /var/lib/suricata/rules/local.rules --> create a local rules file and add the rules already built into the [Suricata rules](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Suricata/Suricata-local.rules) file.
    suricata -c /etc/suricata/suricata.yaml -i eth0  --> runs the suricata with the updated config file as well as updated rules.
   

3. **Issues and Alternatives:**
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
[Proc mail](https://github.com/Distrotech/procmail) Can be used to create mail-servers, mailing lists, sort your incoming mail
into separate folders/files (real convenient when subscribing to one or more
mailing lists or for prioritising your mail), preprocess your mail, start
any programs upon mail arrival (e.g. to generate different chimes on your
workstation for different types of mail) or selectively forward certain
incoming mail automatically to someone.

NEtwork setup for this implememtation:
![Screenshot 2023-11-30 115129](https://github.com/0hex7/IIPP-Internship/assets/108691415/23350eac-544f-4f71-9ff4-cbb114a03de9)



1. **Procmail Installation:**
   ```bash
   sudo apt install procmail
   ```
   All the forwarding recipes must be added to individual users, from whose account, we want to setup email-forwarding if any rule is triggered!
2. **Mail Forwarding Setup:**
   1.  Create rules in `~/.procmailrc` to forward emails with .exe or .zip attachments to `reviewunit` and phishing emails to `susmails`.
   the rules are mentioned in [.procmailrc](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Email-manipulation/.procmailrc), you can copy paste them in your recipe file.
   
   ![Screenshot 2](https://github.com/0hex7/IIPP-Internship/assets/108691415/10129e4d-ea40-400b-ac36-941680604e96)

   2.  Create a procmail.log file in th ehome directory using command touch procmail.log
   3.  Now, we need to modify the configuration file of mail server i.e Postfix to catch commands from the Procmail
       
       sudo rm /etc/postfix/main.cf --> removes old config file
       nano /etc/postfix/main.cf --> Copy paste the contents of [Postfix-main.cf](https://github.com/0hex7/IIPP-Internship/blob/main/Month-3/Postfix/Postfix-main.cf) file to the nano file and save it using CTRL+x
   4. systemctl restart postfix --> restartes the postfix mail server
Now everything is setup, lets do some test emulations and see whats the result!

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
