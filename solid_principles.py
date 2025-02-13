# S.O.L.I.D. principles

# PREREQUISITES:
#   POLYMORPHISM
#   INTERFACES


# I. SINGLE RESPONSIBILITY PRINCIPLE (SRP)

#   Definition: A class should have one, and only one, reason to change.
#   This means that each class should have one specific job or responsibility.
#   This principle emphasizes that each class should focus on a single part of the functionality provided by the software,
#   thereby promoting cohesion and reducing the impact of changes.

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
# user = RefactoredUser("john_doe", "john@example.com")
# validator: Validator = Validator()

# if validator.validate_email(user.email):  # Validation logic
#     user.display_user()  # UI logic
# else:
#     print("Invalid email!")


# II. OPEN / CLOSED PRINCIPLE (OCP)

#   Definition: Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
#   You should be able to add new functionality without changing existing code. Typically achieved through polymorphism and abstraction.

#   Rationale:  Modifying existing code can introduce bugs and unintended side effects.
#   OCP promotes the use of abstractions (interfaces, abstract classes) to allow for extension without modification.


# EXAMPLES

# 1. PaymentProcessor


# Violated version
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount}")
        else:
            raise ValueError("Unsupported payment type")


# Usage
# processor = PaymentProcessor()
# processor.process_payment("credit_card", 100)
# processor.process_payment("paypal", 200)


# Refactored version
class RefactoredPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(RefactoredPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(RefactoredPaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


# Usage
# credit_card_payment: CreditCardPayment = CreditCardPayment()
# credit_card_payment.process_payment(100)

# paypal_payment: PayPalPayment = PayPalPayment()
# paypal_payment.process_payment(200)


# Easily extendable:
class ApplePayPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing Apple Pay payment of ${amount}")


# apple_pay_payment = ApplePayPayment()
# apple_pay_payment.process_payment(150)


# 2. Shape Area Calculation


# Violated version
class AreaCalculator:
    def calculate_area(self, shape):
        if shape["type"] == "circle":
            return 3.14 * shape["radius"] ** 2
        elif shape["type"] == "rectangle":
            return shape["width"] * shape["height"]
        else:
            raise ValueError("Unsupported shape type")


# Usage
# circle = {"type": "circle", "radius": 5}
# rectangle = {"type": "rectangle", "width": 4, "height": 6}

# calculator = AreaCalculator()
# print("Circle Area:", calculator.calculate_area(circle))
# print("Rectangle Area:", calculator.calculate_area(rectangle))


# Refactored version
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class RefactoredAreaCalculator:
    def calculate_shape_area(self, obj_shape: Shape):
        return obj_shape.calculate_area()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.width * self.height


# Usage
# circle: Circle = Circle(radius=5)
# rectangle: Rectangle = Rectangle(width=4, height=6)

# calculator = RefactoredAreaCalculator()
# print("Circle Area:", calculator.calculate_shape_area(circle))
# print("Rectangle Area:", calculator.calculate_shape_area(rectangle))


# # Easily extendable:
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# triangle = Triangle(base=6, height=4)
# print("Triangle Area:", calculator.calculate_shape_area(triangle))


# 3. Logging System


# Violated version
class Logger:
    def log_message(self, message, log_type):
        if log_type == "console":
            print(f"Console log: {message}")
        elif log_type == "file":
            with open("log.txt", "a") as f:
                f.write(f"{message}\n")
        else:
            raise ValueError("Unsupported log type")


# Usage
# logger = Logger()
# logger.log_message("This is a test message", "console")
# logger.log_message("This is another test message", "file")


# Refactored version
class RefactoredLogger(ABC):
    @abstractmethod
    def log_message(self, message):
        pass


class ConsoleLogger(RefactoredLogger):
    def log_message(self, message):
        print(f"Console log: {message}")


class FileLogger(RefactoredLogger):
    def log_message(self, message):
        with open("log.txt", "a") as f:
            f.write(f"{message}\n")


# Usage
# console_logger: ConsoleLogger = ConsoleLogger()
# console_logger.log_message("This is a test message to console")

# file_logger: FileLogger = FileLogger()
# file_logger.log_message("This is a test message to file")


# Easily extendable:
class DatabaseLogger(Logger):
    def log_message(self, message):
        print(f"Saving to database: {message}")  # Placeholder for actual DB write


# db_logger = DatabaseLogger()
# db_logger.log_message("This is a test message to database")
