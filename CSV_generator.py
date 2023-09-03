import random

def CSV_generator():
  """Generates a CSV file with randomly generated inputs."""
  with open("data.csv", "w") as f:
    f.write("name,age,date_of_birth,address,phone_number,email,school\n")
    for i in range(100):
      name = random.choice(["John Doe", "Jane Doe", "Peter Smith", "Susan Jones"])
      age = random.randint(18, 65)
      date_of_birth = f"{random.randint(1950, 2003)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
      address = f"{random.randint(1, 10000)} Main Street, Anytown, CA 12345"
      phone_number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
      email = f"{name}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])}"
      school = f"{random.choice(['Stanford University', 'Harvard University', 'MIT', 'Caltech'])}"
      f.write(f"{name},{age},{date_of_birth},{address},{phone_number},{email},{school}\n")

if __name__ == "__main__":
  generate_csv_file()
