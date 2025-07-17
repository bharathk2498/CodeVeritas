# Risky code to test detection
import os
import subprocess

# This should trigger security alerts
user_input = input("Enter command: ")
os.system(user_input)  # HIGH RISK: Command injection
eval(user_input)       # HIGH RISK: Code evaluation

# Hardcoded secrets
password = "admin123"
api_key = "secret_key_12345"
