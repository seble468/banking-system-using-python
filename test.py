
class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.left = None
        self.right = None


class BankBST:
    def __init__(self):
        self.root = None

    # 🔹 Insert (Create Account)
    def insert(self, root, acc_no, name, balance):
        if root is None:
            return Account(acc_no, name, balance)

        if acc_no < root.acc_no:
            root.left = self.insert(root.left, acc_no, name, balance)
        elif acc_no > root.acc_no:
            root.right = self.insert(root.right, acc_no, name, balance)
        else:
            print(" Account already exists!")

        return root

    # 🔹 Search Account
    def search(self, root, acc_no):
        if root is None or root.acc_no == acc_no:
            return root

        if acc_no < root.acc_no:
            return self.search(root.left, acc_no)
        return self.search(root.right, acc_no)

    # 🔹 Deposit
    def deposit(self, acc_no, amount):
        acc = self.search(self.root, acc_no)
        if acc:
            acc.balance += amount
            print(" Deposit successful.")
        else:
            print(" Account not found.")

    # 🔹 Withdraw
    def withdraw(self, acc_no, amount):
        acc = self.search(self.root, acc_no)
        if acc:
            if acc.balance >= amount:
                acc.balance -= amount
                print(" Withdrawal successful.")
            else:
                print(" Insufficient balance.")
        else:
            print("Account not found.")

    # 🔹 Update Account
    def update(self, acc_no, new_name):
        acc = self.search(self.root, acc_no)
        if acc:
            acc.name = new_name
            print(" Account updated.")
        else:
            print("Account not found.")

    # 🔹 Find minimum (used in delete)
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # 🔹 Delete Account
    def delete(self, root, acc_no):
        if root is None:
            return root

        if acc_no < root.acc_no:
            root.left = self.delete(root.left, acc_no)
        elif acc_no > root.acc_no:
            root.right = self.delete(root.right, acc_no)
        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)
            root.acc_no = temp.acc_no
            root.name = temp.name
            root.balance = temp.balance
            root.right = self.delete(root.right, temp.acc_no)

        return root

    # 🔹 Display (In-order Traversal)
    def display(self, root):
        if root:
            self.display(root.left)
            print(f"Acc No: {root.acc_no}, Name: {root.name}, Balance: {root.balance}")
            self.display(root.right)


# 🔹 Main Menu
def main():
    bank = BankBST()

    while True:
        print("\n====== BANK MENU ======")
        print("1. Create Account")
        print("2. Search Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Update Account")
        print("6. Delete Account")
        print("7. Display Accounts")
        print("8. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            acc_no = int(input("Account Number: "))
            name = input("Name: ")
            balance = float(input("Balance: "))
            bank.root = bank.insert(bank.root, acc_no, name, balance)

        elif choice == 2:
            acc_no = int(input("Enter Account Number: "))
            acc = bank.search(bank.root, acc_no)
            if acc:
                print(f"Found → Name: {acc.name}, Balance: {acc.balance}")
            else:
                print(" Account not found.")

        elif choice == 3:
                    acc_no = int(input("Account Number: "))
                    amount = float(input("Amount: "))
                    bank.deposit(acc_no, amount)

        elif choice == 4:
                    acc_no = int(input("Account Number: "))
                    amount = float(input("Amount: "))
                    bank.withdraw(acc_no, amount)

        elif choice == 5:
                    acc_no = int(input("Account Number: "))
                    name = input("New Name: ")
                    bank.update(acc_no, name)

        elif choice == 6:
                    acc_no = int(input("Account Number: "))
                    bank.root = bank.delete(bank.root, acc_no)
                    print("Account deleted (if it existed).")

        elif choice == 7:
                    print("\n--- All Accounts (Sorted) ---")
                    bank.display(bank.root)

        elif choice == 8:
                    print("Exiting system...")
                    break

main()
