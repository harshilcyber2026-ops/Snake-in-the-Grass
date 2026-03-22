# FLAGVAULT REVERSE ENGINEERING TASK: 001
import base64

def check_access():
    # Hidden Key: quantum_entropy_2026
    # Flag: FlagVault{PY_REVERSE_MASTER_99}
    
    encoded_key = "cXVhbnR1bV9lbnRyb3B5XzIwMjY="
    user_input = input("Enter Access Key to decrypt flag: ")
    
    if base64.b64encode(user_input.encode()).decode() == encoded_key:
        # The flag is stored as an integer array to avoid 'grep' detection
        secret_hex = [0x46, 0x6c, 0x61, 0x67, 0x56, 0x61, 0x75, 0x6c, 0x74, 0x7b, 0x50, 0x59, 0x5f, 0x52, 0x45, 0x56, 0x45, 0x52, 0x53, 0x45, 0x5f, 0x4d, 0x41, 0x53, 0x54, 0x45, 0x52, 0x5f, 0x39, 0x39, 0x7d]
        print("\n[+] ACCESS GRANTED")
        print("FLAG: " + "".join(chr(x) for x in secret_hex))
    else:
        print("\n[!] ACCESS DENIED: Invalid Key.")

if __name__ == "__main__":
    check_access()