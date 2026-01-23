from faker import Faker

fake = Faker()

def get_registered_user():
    return {
        "customer_name":fake.name(),
        "customer_address":fake.address(),
        "registered_on":fake.year()

    }
if __name__=="__main__":
    print(get_registered_user())