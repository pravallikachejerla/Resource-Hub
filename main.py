
import json


resources = [
    {
        "name": "Food Pantry",
        "location": "123 Main Street, Anytown, USA",
        "description": "Provides free groceries to families in need.",
        "contact": "Phone: (123) 456-7890"
    },
    {
        "name": "Free Clinic",
        "location": "456 Elm Avenue, Anytown, USA",
        "description": "Offers free healthcare services including checkups and vaccinations.",
        "contact": "Phone: (456) 789-0123"
    },
    {
        "name": "Education Center",
        "location": "789 Oak Road, Anytown, USA",
        "description": "Provides tutoring and educational resources for students.",
        "contact": "Phone: (789) 012-3456"
    },
    {
        "name": "Emergency Shelter",
        "location": "321 Pine Boulevard, Anytown, USA",
        "description": "Offers temporary housing and support services for homeless individuals.",
        "contact": "Phone: (321) 654-9870"
    },
    {
        "name": "Legal Aid Clinic",
        "location": "654 Cedar Lane, Anytown, USA",
        "description": "Provides free legal assistance and advice to low-income individuals.",
        "contact": "Phone: (654) 987-3210"
    },
    {
        "name": "Community Soup Kitchen",
        "location": "987 Willow Street, Anytown, USA",
        "description": "Serves hot meals daily to individuals and families in need.",
        "contact": "Phone: (987) 321-6540"
    }
]

# Sample user data for registration and login
users = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def display_resources():
    """Displays available essential resources."""
    print("\nAvailable Resources:")
    for idx, resource in enumerate(resources, start=1):
        print(f"\nResource {idx}:")
        print(f"Name: {resource['name']}")
        print(f"Location: {resource['location']}")
        print(f"Description: {resource['description']}")
        print(f"Contact: {resource['contact']}")

def find_resource_by_name(name):
    """Finds a resource by name."""
    for resource in resources:
        if resource['name'].lower() == name.lower():
            return resource
    return None

def register():
    """Registers a new user."""
    print("\nRegister:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    users.append(User(username, password))
    print("Registration successful!")

def login():
    """Logs in an existing user."""
    print("\nLogin:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.username == username and user.password == password:
            print(f"Welcome, {username}!")
            return user
    print("Login failed. Invalid username or password.")
    return None

def main():
    print("Welcome to CommunityConnect - Connecting Underserved Communities!")

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. View Available Resources")
        print("4. Find a Specific Resource")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()

        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\nResource Menu:")
                    print("1. Display Available Resources")
                    print("2. Find a Specific Resource")
                    print("3. Logout")
                    resource_choice = input("Enter your choice: ")

                    if resource_choice == '1':
                        display_resources()

                    elif resource_choice == '2':
                        resource_name = input("Enter the name of the resource: ")
                        resource = find_resource_by_name(resource_name)
                        if resource:
                            print("\nResource Found:")
                            print(f"Name: {resource['name']}")
                            print(f"Location: {resource['location']}")
                            print(f"Description: {resource['description']}")
                            print(f"Contact: {resource['contact']}")
                        else:
                            print(f"Resource '{resource_name}' not found.")

                    elif resource_choice == '3':
                        print(f"Logging out user {user.username}...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            display_resources()

        elif choice == '4':
            resource_name = input("Enter the name of the resource: ")
            resource = find_resource_by_name(resource_name)
            if resource:
                print("\nResource Found:")
                print(f"Name: {resource['name']}")
                print(f"Location: {resource['location']}")
                print(f"Description: {resource['description']}")
                print(f"Contact: {resource['contact']}")
            else:
                print(f"Resource '{resource_name}' not found.")

        elif choice == '5':
            print("Exiting CommunityConnect. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
