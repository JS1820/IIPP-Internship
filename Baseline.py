import requests
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Define the URL of the login page
url = "https://140.113.110.151:64294/cockpit/login"
password = "username:password" # Please enter the correct username and password here!

# Encode the password in Base64
encoded_password = base64.b64encode(password.encode()).decode()
#print(encoded_password)
# Set the headers with the Authorization token
headers = {
    'Authorization': f'Basic {encoded_password}',
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'  # Replace with a valid User-Agent
}

try:
    # Send the login request without SSL certificate verification and with headers
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:#  and "csrf-token" in response.text:
        # The authentication was successful, and a CSRF token is present in the HTML response
        print("Authentication successful")
        #print("Response Content:", response.text)
    else:
        # The authentication failed or the CSRF token is not found in the response
        print("Authentication failed")
        #print("Response Content:", response.text)

        # Execute the script to stop and start the VM
        
        print("Suspending the virtual machine...")
        subprocess.call([
            "C:/Program Files (x86)/VMware/VMware Player/vmrun.exe",
            "suspend",
            "C:/Users/user/Documents/Virtual Machines/Tpot/Tpot.vmxf"
        ])
        print("Starting the virtual machine...")
        subprocess.call([
            "C:/Program Files (x86)/VMware/VMware Player/vmrun.exe",
            "start",
            "C:/Users/user/Documents/Virtual Machines/Tpotbaseline/baseline.vmxf"
        ])

except requests.exceptions.RequestException as e:
    print(f"An error occurred with the HTTP request: {e}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred when executing vmrun: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

