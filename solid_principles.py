# S.O.L.I.D. principles

# PREREQUISITES:
#   POLYMORPHISM
#   INTERFACES


# I. Single Responsibility Principle (SRP)

#   Definition: A class should have one, and only one, reason to change.
#   This means that each class should have one specific job or responsibility.

#   Rationale:  Changes to one part of a class shouldn't necessitate changes to unrelated parts.
#   This improves code clarity, reduces the risk of introducing bugs, and makes testing easier.


# EXAMPLES

from abc import ABC, abstractmethod

# 1. ORDER CLASS


# Violated version
class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        return sum(item["price"] for item in self.items)

    def save_to_database(self):
        print("Saving order to database...")

    def send_confirmation_email(self):
        print("Sending order confirmation email...")


# Usage
# order = Order(
#     [
#         {"name": "MacBook Pro 13", "price": 2500},
#         {"name": "iphone 17 Pro Max", "price": 2000},
#         {"name": "AirPods Pro 3", "price": 250},
#     ]
# )
# print("Total Price:", order.calculate_total_price())  # Business logic
# order.save_to_database()  # Persistence
# order.send_confirmation_email()  # Notification


# Refactored version
#   Solution: NOT separate class methods, but declare interfaces to not break Order class when modifying methods
#   * Interface creating for Order class and its calculate_total_price() were skipped for simplicity


# Create interfaces
class SaveOrder(ABC):
    @abstractmethod
    def save_order(self):
        pass


class NotifyUser(ABC):
    @abstractmethod
    def send_confirmation(self):
        pass


# Override methods for every notification and save type
class SaveToDb(SaveOrder):
    def save_order(self):
        print("Saving order to database...")


class SaveToCsv(SaveOrder):
    def save_order(self):
        print("Saving order to CSV file...")


class NotifyByEmail(NotifyUser):
    def send_confirmation(self):
        print("Sending order confirmation email...")


# Use interfaces in main class
class RefactoredOrder:
    def __init__(self, items):
        self.items = items

    def calculate_total_price(self):
        return sum(item["price"] for item in self.items)

    def save_order(self, save_method: SaveOrder):
        save_method.save_order()

    def send_confirmation(self, notification_method: NotifyUser):
        notification_method.send_confirmation()


# Usage
# refactored_order = RefactoredOrder(
#     [
#         {"name": "MacBook Pro 13", "price": 2500},
#         {"name": "iphone 17 Pro Max", "price": 2000},
#         {"name": "AirPods Pro 3", "price": 250},
#     ]
# )
# print("Total Price:", refactored_order.calculate_total_price())  # Business logic

# save_to_db: SaveToDb = SaveToDb()
# save_to_csv: SaveToCsv = SaveToCsv()

# refactored_order.save_order(save_to_db)  # Persistence
# refactored_order.save_order(save_to_csv)  # Persistence

# notify_by_email: NotifyByEmail = NotifyByEmail()

# refactored_order.send_confirmation(notify_by_email)  # Notification


# 2. REPORT


# Violated version
class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate_report())

    def send_to_printer(self):
        print("Sending report to printer...")


# Usage
# report = Report("Sales Data for Q1")
# print(report.generate_report())  # Report generation
# report.save_to_file("report.txt")  # File handling
# report.send_to_printer()  # Printing


# Refactored version
class RefactoredReport:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"


class SaveReport:
    def save_to_file(self, filename, report_data):
        with open(filename, "w") as f:
            f.write(report_data)


class OutputReport:
    def send_to_printer(self):
        print("Sending report to printer...")


# # Usage
# report = RefactoredReport("Sales Data for Q1")
# report_data = report.generate_report()
# print(report_data)  # Report generation

# save_report: SaveReport = SaveReport()
# save_report.save_to_file(filename="report.txt", report_data=report_data)  # File handling

# output_report: OutputReport = OutputReport()
# output_report.send_to_printer()  # Printing


# 3. USER


# Violated version
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def validate_email(self):
        return "@" in self.email

    def display_user(self):
        print(f"User: {self.username}, Email: {self.email}")


# # Usage
# user = User("john_doe", "john@example.com")
# if user.validate_email():  # Validation logic
#     user.display_user()  # UI logic
# else:
#     print("Invalid email!")


# Refactored version
class RefactoredUser:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_user(self):
        print(f"User: {self.username}, Email: {self.email}")


class Validator:
    @staticmethod
    def validate_email(email):
        return "@" in email


# Usage
user = RefactoredUser("john_doe", "john@example.com")
validator: Validator = Validator()

if validator.validate_email(user.email):  # Validation logic
    user.display_user()  # UI logic
else:
    print("Invalid email!")
