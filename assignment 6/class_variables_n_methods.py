class Bank:   
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

customer1 = Bank("Abiha")
customer2 = Bank("Hassan")

customer1.show_info()
customer2.show_info()

Bank.change_bank_name("Global Trust Bank")

print("\nAfter changing bank name:\n")
customer1.show_info()
customer2.show_info()

    