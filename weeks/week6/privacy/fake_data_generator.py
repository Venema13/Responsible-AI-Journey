# Week 6: Fake Data Generator using Faker library
from faker import Faker

fake = Faker()

def generate_fake_data(n=5):
    """Generate n fake names, emails, and phone numbers."""
    data = []
    for _ in range(n):
        entry = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }
        data.append(entry)
    return data

if __name__ == "__main__":
    fake_entries = generate_fake_data(5)
    for e in fake_entries:
        print(e)
