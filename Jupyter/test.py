import json

# Function to load usernames and passwords from JSON file
def load_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

# Function to save usernames and passwords to JSON file
def save_credentials(credentials, filename):
    with open(filename, 'w') as file:
        json.dump(credentials, file)

# Example usage
# Initialize credentials dictionary
credentials = {}

# Add username and password
credentials['user1'] = 'password1'
credentials['user2'] = 'password2'

# Save credentials to JSON file
save_credentials(credentials, 'credentials.json')

# Load credentials from JSON file
loaded_credentials = load_credentials('credentials.json')
print("Loaded credentials:", loaded_credentials)

