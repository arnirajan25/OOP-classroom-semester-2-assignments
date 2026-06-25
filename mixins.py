#Mixins Create two mixins: LoggerMixin (adds a log() method) and SerializerMixin (adds a serialize() Create two method). Combine them with a User class. Demonstrate logging and serialization.
import json

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] [{self.__class__.__name__}]: {message}")

class SerializerMixin:
    def serialize(self):
        public_data = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return json.dumps(public_data, indent=2)

class User(LoggerMixin, SerializerMixin):
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role
        self.log(f"New user profile successfully generated for {self.username}.")

    def update_email(self, new_email):
        self.email = new_email
        self.log(f"Email updated to: {new_email}")

if __name__ == "__main__":
    print("--- Initializing User Class (Triggering LoggerMixin) ---")
    user = User(username="arnirajan", email="nirajan@example.com", role="Student")

    print("\n--- Executing Business Logic (Triggering LoggerMixin) ---")
    user.update_email("nirajanaryal@example.com")

    print("\n--- Exporting Data Structure (Triggering SerializerMixin) ---")
    json_output = user.serialize()
    print("Serialized JSON String Output:")
    print(json_output)
