import string  # Import the string module

# Define the characters for digits
digits = string.digits

# Define the pattern with placeholders
prefix = "Nycuaiserver@"   # You can give any custom prefix to generate passwords based on it.
suffix_length = 3  # Number of digits to add

# Generate passwords and save them to a .txt file
with open("C:/Users/user/Desktop/passwordlist.txt", "w") as file:
    for i in range(10**suffix_length):  # Generate passwords with all combinations of three digits (000 to 999)
        password = f"{prefix}{i:0{suffix_length}}"
        file.write(password + "\n")

print("Passwords saved to passwordlist.txt")
