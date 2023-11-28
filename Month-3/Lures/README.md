# Lures Implementation in Tpot CE Honeypot

## Description of the Environment

We will be focusing on the cowrie honeypot container, which is up and running in Tpot CE Honeypot. Cowrie is running on ports 21 and 22.

We ran into a 'Read-only file system' error in the previous week!

We will be trying to solve that error and implement lures in the cowrie honeypot, running on ports 21 and 22 of our Tpot CE honeypot.

## Setting Up Lures in Cowrie Honeypot

In this phase, we focus on implementing lures within the Cowrie honeypot to attract and engage potential attackers. The goal is to create an environment that entices attackers, captures their activities, and provides valuable insights for analysis.

### Initial Setup

1. **Honeypot IP Address:**
   - The IP address of the Tpot honeypot is set to `140.113.110.151`.
   - Connected to the router using a static IP.

2. **ELK Stack Configuration:**
   - ELK Stack is configured to run in sync with Tpot at `140.113.110.151:64297`.

3. **Kali Attacks on Tpot:**
   - Utilized Kali Linux to perform attacks on the Tpot honeypot.
   - Executed Hydra attack on port 22 for SSH connection.
   - Attempted connection via port 22 using password `123456`.
   - Explored the `/etc/passwd` file.
   ![Screenshot 2023-10-22 003615](https://github.com/0hex7/IIPP-Internship/assets/108691415/42848f9a-5f4c-4cfe-a169-0e04eb76f485)

### Understanding the Need for Lures

1. **Phil Association:**
   - Identified that the name "Phil" is widely associated with the Cowrie honeypot file system.
   - Recognized the necessity to create a different file system to enhance the honeypot's attractiveness.

### Configuration of Lures in Cowrie

1. **Understand and Solve the Error:**
   ![Screenshot 2023-10-23 022852](https://github.com/0hex7/IIPP-Internship/assets/108691415/131d7d25-5fe1-4570-a1b2-28caea343e44)
   - If we try to change the file system in Tpot honeypot by executing the cowrie, we get an error 'Read-only file system'
   - This is because the cowrie container in Tpot is already built (as a read-only file system), so we cannot make any modifications while it's running.
   ![Screenshot 2023-10-22 184814](https://github.com/0hex7/IIPP-Internship/assets/108691415/ed7ed3b8-9fe6-4774-9596-8563a992a91c)

2. **Solve the Error:**
   - Stop and remove the docker container cowrie.
   - `docker stop cowrie`
   - `docker rm cowrie`
   - `sudo nano /opt/tpot/docker/cowrie/docker-compose.yml`
   - In the compose file, change a few lines as given in the below picture -- refer [cowrie-docker-compose.yml](https://github.com/0hex7/IIPP-Internship/new/main/Month-3/Lures/Cowrie-docker-compose.yml)
   ![Screenshot 2023-10-29 000725](https://github.com/0hex7/IIPP-Internship/assets/108691415/36f2c4ca-7bf7-436a-b368-cbf5b36ceb0c)
   - `docker-compose build cowrie`
   - `docker-compose up -d cowrie`
   Now, the error is solved, and we can continue with setting up our lures in the cowrie honeypot!

3. **Setup Lures Inside the Cowrie Honeypot**
   - `cd /opt/tpot/docker/cowrie`
   - `docker exec -it cowrie /bin/bash` --> we are inside the cowrie container environment
   - `cd /home`
   - `rm -rf phil` --> we removed the default phil file system
   - `mkdir wu-chen`
   - `mkdir admin`
   - `mkdir user` --> we created 3 new users for the cowrie file system
   - `cd wu-chen/` --> we can add any kinds of lures inside the directory.
   ![Screenshot 2023-11-29 005516](https://github.com/0hex7/IIPP-Internship/assets/108691415/1c42f0ab-d10b-4bcb-9d22-863a1708ca38)
   - With this, we have set up the file system for the cowrie honeypot.

4. **Fake Commands:**
   - Explored preconfigured fake commands in `./share/cowrie/txtcmds`.
   - Recognized the importance of these commands and added a few more commands to the list.
   ![Screenshot 2023-10-29 160919](https://github.com/0hex7/IIPP-Internship/assets/108691415/08296b22-d1c6-4eb3-b072-302c1d22b3bb)

5. **Honeypot Filesystem:**
   - Explored the honeypot filesystem in `./honeyfs`.
   - Added the newly added users' data into the /etc/passwd file for more authenticity.

6. **Pickle Filesystem:**
   - Investigated the pickle filesystem in `./share/cowrie/fs.pickle`.
   - Various files like password.keys and cryptowallet.keys were added to the .pickle fs, to enhance the deception ability of the honeypot.
   ![Screenshot 2023-10-30 021355](https://github.com/0hex7/IIPP-Internship/assets/108691415/96cf7d6d-cf53-4649-bfd9-ed76d58d6d92)
   ![Screenshot 2023-10-30 004432](https://github.com/0hex7/IIPP-Internship/assets/108691415/664325a0-01e9-4998-97d9-5187bbd10ca7)

### Overall Implementation Process

1. **Creation of a New fs.pickle:**
   - Encountered an error due to the Docker container being in a read-only state.
   - Resolved the error by configuring the `docker-compose.yml` file.

2. **Verification and Access:**
   - Verified the container status using `dps.sh`.
   - Accessed the container filesystem and identified the directories requiring setup.

3. **Lures Setup:**
   - Focused on `honeyfs/etc/passwd` and `shadow` files from the host system.
   - Added three new users to make the system more authentic.
   - Ensured visibility in the cowrie honeypot by implementing users in `fs.pickle` as well.

4. **Finalization:**
   - Set up lures to waste attackers' time effectively.
   - Implemented files in `fs.pickle` to attract attackers.
   - Successfully mimicked a realistic environment for attackers to explore.

### Attackers' Perspective

1. **Nmap Scan and SSH Connection:**
   - Attacker performs an Nmap scan on the honeypot IP.
   - Attempts SSH connection to the honeypot.

2. **File Exploration:**
   - Attacker explores the `/etc/passwd` file in the cowrie honeypot.

3. **Command Responses:**
   - Displays pre-configured command responses from `txtcmds` folder.

4. **Lures Effectiveness:**
   - Demonstrates the visibility of files in `fs.pickle` and the limitation of accessing real files in `honeyfs`.
   ![Screenshot 2023-10-30 031514](https://github.com/0hex7/IIPP-Internship/assets/108691415/a7b23d9d-fc29-45b5-b305-70bbf11849f9)

### Conclusion

The successful implementation of lures within the Cowrie honeypot enhances the environment's authenticity, attracting potential attackers and providing valuable insights for further analysis. The integration of realistic scenarios strengthens the honeypot's ability to capture diverse attack patterns.
