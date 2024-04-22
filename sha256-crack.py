from pwn import *  # pwn is a library used for exploitation tasks, here primarily for its logging capabilities
import sys  # sys is used to access command-line arguments

# Check if the correct number of command-line arguments has been provided
if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0]))  # Display correct usage format if incorrect
    exit()  # Exit the script if the number of arguments is incorrect

target_hash = sys.argv[1]  # Store the SHA-256 hash provided as a command-line argument
print(target_hash)  # Print the target hash
password_list_path = "10-million-password-list-top-100.txt"  # Specify the password file to use
attempt_counter = 0  # Initialize a counter for the number of password attempts

# Begin a progress log for the password cracking attempt, using the pwn library for visual feedback
with log.progress("Attempting to hack: {}!\n".format(target_hash)) as progress:
    # Open the password list file in read mode with 'latin-1' encoding
    with open(password_list_path, "r", encoding='latin-1') as file:
        for password in file:
            password_cleaned = password.strip("\n").encode('latin-1')  # Remove newline characters and encode the password
            current_password_hash = sha256sumhex(password_cleaned)  # Compute the SHA-256 hash of the password
            # Update the progress log with the current attempt's details
            progress.status("[{}] {} == {}".format(attempt_counter, password_cleaned.decode('latin-1'), current_password_hash))
            if current_password_hash == target_hash:
                # If the hash of the current password matches the target hash, announce success and exit
                progress.success("Password hash found after {} attempts! {} hashes to {}!".format(attempt_counter, password_cleaned.decode('latin-1'), current_password_hash))
                exit()
            attempt_counter += 1  # Increment the attempt counter
        # If the loop completes without finding a match, announce failure
        progress.failure("Password hash not found!")