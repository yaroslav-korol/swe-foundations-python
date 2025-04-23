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


#  III. LISKOV SUBSTITUTION PRINCIPLE (LSP)

#   Definition: Objects of a derived (child- sub-) class should be substitutable for objects of their
#   base (super- parent-) class without altering any of the desirable properties of that program.

#   Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
#   In other words, subclasses should enhance, not weaken, the functionality of the base class,
#   ensuring that derived classes uphold the promises made by the base class.

#   Rationale:  If subtypes are not substitutable for their base types, it can lead to unexpected behavior
#   and break code that relies on the base type.  This principle ensures that inheritance is used correctly.


# EXAMPLES

# 1. Bird Behavior


# Violated version
class Bird:
    def fly(self):
        print("Flying in the sky!")


class Sparrow(Bird):
    pass  # Sparrow can fly, so it works fine


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly!")  # Violates LSP


# Usage
def make_bird_fly(bird: Bird):
    bird.fly()


# sparrow = Sparrow()
# penguin = Penguin()

# make_bird_fly(sparrow)  # Works fine
# make_bird_fly(penguin)  # Throws an exception, violating LSP


# Refactored version


class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass


class SwimmingBird(ABC):
    @abstractmethod
    def swim(self):
        pass


class Hawk(FlyingBird):
    def fly(self):
        print("Flying in the sky!")


class ChillyWillyPenguin(SwimmingBird):
    def swim(self):
        print("Swimming in the lake!")


# Usage
def let_bird_fly(bird: FlyingBird):
    bird.fly()


def let_bird_swim(bird: SwimmingBird):
    bird.swim()


# hawk: Hawk = Hawk()
# chilly_willy_penguin: ChillyWillyPenguin = ChillyWillyPenguin()

# let_bird_fly(hawk)
# let_bird_swim(chilly_willy_penguin)


# Easily extendable:
class Duck(FlyingBird, SwimmingBird):
    def fly(self):
        print("Flying in the sky!")

    def swim(self):
        print("Swimming in the lake!")


# donald_duck: Duck = Duck()

# let_bird_fly(donald_duck)
# let_bird_swim(donald_duck)


# 2. Rectangle and Square


# Violated version
class DefaultRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class DefaultSquare(DefaultRectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Forces height to be the same, breaking expected behavior

    def set_height(self, height):
        self.width = height
        self.height = height  # Forces width to be the same, breaking expected behavior


# Usage
def print_area(rectangle: DefaultRectangle):
    rectangle.set_width(5)
    rectangle.set_height(10)
    print(f"Area: {rectangle.get_area()}")


# rect = DefaultRectangle(2, 3)
# square = DefaultSquare(4, 4)

# print_area(rect)  # Expected output: Area: 50
# print_area(square)  # Unexpected output, violates LSP


# Refactored version
class DefaultShape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class RefactoredRectangle(DefaultShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height


class RefactoredSquare(DefaultShape):
    def __init__(self, width):
        self.width = width

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.width


# Usage
def print_shape_area(rectangle: DefaultShape):
    print(f"Area: {rectangle.get_area()}")


# refactored_rectangle: RefactoredRectangle = RefactoredRectangle(height=2, width=3)
# refactored_square = RefactoredSquare(width=4)

# print_shape_area(refactored_rectangle)
# print_shape_area(refactored_square)

# refactored_rectangle.set_height(5)
# refactored_rectangle.set_width(10)
# refactored_square.set_width(10)

# print_shape_area(refactored_rectangle)
# print_shape_area(refactored_square)


# 3. Payment System


# Violated version
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def refund_payment(self, amount):
        print(f"Refunding payment of ${amount}")


class DefaultCreditCardPayment(PaymentProcessor):
    pass  # Supports both payments and refunds


class CryptoPaymentProcessor(PaymentProcessor):
    def refund_payment(self, amount):
        raise Exception("Refunds not supported for crypto payments!")  # Violates LSP


# Usage
def process_and_refund(processor: PaymentProcessor, amount):
    processor.process_payment(amount)
    processor.refund_payment(amount)


# credit_card = DefaultCreditCardPayment()
# crypto = CryptoPaymentProcessor()

# process_and_refund(credit_card, 100)  # Works fine
# process_and_refund(crypto, 200)  # Throws exception, violating LSP


# Refactored version
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class RefundProcessor(ABC):
    @abstractmethod
    def refund_payment(self, amount: float):
        pass


class ChargeBackProcessor(ABC):
    @abstractmethod
    def open_chargeback(self, amount: float):
        pass


class RefactoredCreditCardPayment(PaymentProcessor, RefundProcessor, ChargeBackProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing card payment of ${amount}")

    def refund_payment(self, amount: float) -> None:
        print(f"Refunding card payment of ${amount}")

    def open_chargeback(self, amount: float) -> None:
        print(f"Open dispute on card payment of ${amount}")


class RefactoredCryptoPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing crypto payment of ${amount}")


# Usage
def process_transaction(processor: PaymentProcessor, amount: float) -> None:
    processor.process_payment(amount)


def refund_transaction(processor: RefundProcessor, amount: float) -> None:
    processor.refund_payment(amount)


def dispute_transaction(processor: ChargeBackProcessor, amount) -> None:
    processor.open_chargeback(amount)


# credit_card_payment: RefactoredCreditCardPayment = RefactoredCreditCardPayment()
# crypto_payment: RefactoredCryptoPayment = RefactoredCryptoPayment()

# process_transaction(credit_card_payment, 100)
# refund_transaction(credit_card_payment, 25)
# dispute_transaction(credit_card_payment, 25)

# process_transaction(crypto_payment, 200)


# Easy extend
class RefactoredPayPalPayment(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")

    def refund_payment(self, amount: float) -> None:
        print(f"Refunding PayPal payment of ${amount}")


# paypal_payment: RefactoredPayPalPayment = RefactoredPayPalPayment()
# process_transaction(paypal_payment, 321)
# refund_transaction(paypal_payment, 123)


# IV. Interface Segregation Principle (ISP)

#   Definition: Clients should not be forced to depend on interfaces that they do not use.
#   Instead, many specific interfaces are better than one general interface.

#   Rationale:  Large, "fat" interfaces can lead to classes implementing methods they don't need, creating unnecessary dependencies and coupling.
#   ISP promotes creating smaller, more focused interfaces that clients can use selectively.

#   This principle advocates for creating specific interfaces
#   tailored to client needs rather than a one-size-fits-all interface, thereby reducing the impact of changes and promoting decoupling.

# Possible solutions: 1)use separate interfaces; 2)hierarchy of interfaces


# EXAMPLES

# 1. Printer


# Violated version
class MultifunctionPrinter:
    def print_document(self, document):
        pass

    def scan_document(self, document):
        pass

    def fax_document(self, document):
        pass


class BasicPrinter(MultifunctionPrinter):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        raise Exception("Scanning not supported!")  # ISP violation

    def fax_document(self, document):
        raise Exception("Faxing not supported!")  # ISP violation


# Usage
def use_printer(printer: MultifunctionPrinter):
    printer.print_document("Report.pdf")
    printer.scan_document("Report.pdf")  # Will throw an exception if BasicPrinter is passed
    printer.fax_document("Report.pdf")  # Will throw an exception if BasicPrinter is passed


# basic_printer = BasicPrinter()
# use_printer(basic_printer)  # ❌ Breaks ISP - BasicPrinter cannot scan or fax


# Refactored Version
class Printer(ABC):
    @abstractmethod
    def print_document(self, document) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document) -> None:
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self, document) -> None:
        pass


class MultifunctionProduct(Printer, Scanner, Fax):
    def print_document(self, document) -> None:
        print(f"Printing: {document}")

    def scan_document(self, document) -> None:
        print(f"Scanning: {document}")

    def fax_document(self, document) -> None:
        print(f"Faxing: {document}")


# Usage
def print_copy(printer: Printer, doc) -> None:
    printer.print_document(doc)


def scan_copy(scanner: Scanner, doc) -> None:
    scanner.scan_document(doc)


def send_fax(fax: Fax, doc) -> None:
    fax.fax_document(doc)


# hp_printer: MultifunctionProduct = MultifunctionProduct()
# print_copy(hp_printer, "Report.pdf")
# hp_printer.print_document("Report.pdf")
# hp_printer.scan_document("Report.pdf")
# hp_printer.fax_document("Report.pdf")


# Easy extend
class PrinterWithScanner(Printer, Scanner):
    def print_document(self, document) -> None:
        print(f"Printing: {document}")

    def scan_document(self, document) -> None:
        print(f"Scanning: {document}")


# canon_printer_scanner: PrinterWithScanner = PrinterWithScanner()

# canon_printer_scanner.print_document("doc.txt")
# canon_printer_scanner.scan_document("doc.txt")
# print_copy(canon_printer_scanner, "doc.txt")
# scan_copy(canon_printer_scanner, "doc.txt")


# 2. Worker Example


# Violated version
class Worker:
    def work(self):
        pass

    def eat(self):
        pass


class Robot(Worker):
    def work(self):
        print("Robot working.")

    def eat(self):
        raise Exception("Robots don't eat!")  # ISP violation


# Usage
def break_time(worker: Worker):
    worker.eat()  # Will break if Robot is passed


# robot_worker = Robot()
# break_time(robot_worker)  # ❌ Breaks ISP - Robots don't eat


# Refactored version
class BaseWorker(ABC):
    @abstractmethod
    def start_work(self):
        pass

    @abstractmethod
    def stop_work(self):
        pass


class HumanBeing(ABC):
    @abstractmethod
    def eat(self):
        pass


class RobotWorker(BaseWorker):
    def start_work(self):
        print("Robot working.")

    def stop_work(self):
        print("Robot taking break from work.")


class HumanWorker(BaseWorker, HumanBeing):
    def start_work(self):
        print("Human working.")

    def stop_work(self):
        print("Human taking break from work.")

    def eat(self):
        print("Human eating!")


# Usage
def break_work(worker: BaseWorker):
    worker.stop_work()


# robot_worker: RobotWorker = RobotWorker()
# human_worker: HumanWorker = HumanWorker()

# break_work(robot_worker)
# break_work(human_worker)


# 3. Vehicle Example


# Violated version
class Vehicle:
    def refuel(self):
        pass

    def charge_battery(self):
        pass


class PetrolCar(Vehicle):
    def refuel(self):
        print("Refueling petrol car.")

    def charge_battery(self):
        raise Exception("Petrol cars don't have batteries to charge!")  # ISP violation


class ElectricCar(Vehicle):
    def charge_battery(self):
        print("Charging electric car.")

    def refuel(self):
        raise Exception("Electric cars don’t use fuel!")  # ISP violation


# Usage
def refill(vehicle: Vehicle):
    vehicle.refuel()  # Will break if an ElectricCar is passed


def recharge(vehicle: Vehicle):
    vehicle.charge_battery()  # Will break if a PetrolCar is passed


# tesla = ElectricCar()
# bmw = PetrolCar()

# refill(tesla)  # ❌ Breaks ISP - Electric cars don’t use fuel
# recharge(bmw)  # ❌ Breaks ISP - Petrol cars don’t have a battery to charge


# Refactored version
class BaseVehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Refuelable(ABC):
    @abstractmethod
    def refuel(self):
        pass


class Rechargeable(ABC):
    @abstractmethod
    def charge_battery(self):
        pass


class OrdinaryCar(BaseVehicle, Refuelable):
    def move(self):
        print("Patrol car moving")

    def stop(self):
        print("Patrol car not moving")

    def refuel(self):
        print("Refueling petrol car.")


class ElectricalCar(BaseVehicle, Rechargeable):
    def move(self):
        print("Electric car moving")

    def stop(self):
        print("Electric car not moving")

    def charge_battery(self):
        print("Charging electric car.")


# Usage
def refill_car(vehicle: Refuelable):
    vehicle.refuel()


def recharge_car(vehicle: Rechargeable):
    vehicle.charge_battery()


# tesla_car: ElectricalCar = ElectricalCar()
# bmw_car: OrdinaryCar = OrdinaryCar()

# refill(bmw_car)
# recharge(tesla_car)


# Easy extend
def drive_car(car: BaseVehicle):
    car.move()
    car.stop()


# drive_car(tesla_car)
# drive_car(bmw_car)


# V. DEPENDENCY INVERSION PRINCIPLE (DIP)

#   Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions.
#   Additionally, abstractions should not depend on details; details should depend on abstractions.

#   Rationale:  DIP decouples high-level modules from low-level modules by introducing abstractions.
#   This makes the system more flexible, reusable, and easier to test.
#   Changes to low-level modules are less likely to impact high-level modules.
#   This principle encourages the decoupling of software modules by introducing abstract layers between high-level and low-level modules.


# Examples


# 1. Payment Processing
# Violated version
class PayPalPaymentProcessor:
    def process_payment(self, amount: float):
        print(f"Processing ${amount} payment through PayPal.")


class OnlineStore:
    def __init__(self):
        self.payment_processor = PayPalPaymentProcessor()  # ❌ Violates DIP

    def checkout(self, amount: float):
        self.payment_processor.process_payment(amount)


# Usage
# store = OnlineStore()
# store.checkout(100.0)  # ❌ Hardcoded PayPal dependency


# Refactored version
class GatewayPaymentProcessor(ABC):
    @abstractmethod
    def make_payment(self, amount: float):
        pass


class PayPalProcessor(GatewayPaymentProcessor):
    def make_payment(self, amount: float):
        print(f"Processing ${amount} payment through PayPal.")


class DigitalStore:
    def __init__(self, payment_processor: GatewayPaymentProcessor):
        self.payment_processor: GatewayPaymentProcessor = payment_processor

    def checkout(self, amount: float):
        self.payment_processor.make_payment(amount)


# Usage
# current_processor: GatewayPaymentProcessor = PayPalProcessor()
# store = DigitalStore(current_processor)
# store.checkout(100.0)


# Easy extendable
class StripeProcessor(GatewayPaymentProcessor):
    def make_payment(self, amount: float):
        print(f"Processing ${amount * 100} cents payment through Stripe.")


# Usage
# new_processor: GatewayPaymentProcessor = StripeProcessor()
# store = DigitalStore(new_processor)
# store.checkout(200.0)


# 2. Notification System


# Violated version
class EmailNotifier:
    def send_email(self, message: str):
        print(f"Sending email: {message}")


class UserService:
    def __init__(self):
        self.notifier = EmailNotifier()  # ❌ Violates DIP

    def notify_user(self, message: str):
        self.notifier.send_email(message)


# Usage
# user_service = UserService()
# user_service.notify_user("Welcome!")  # ❌ Hardcoded email notification


# Refactored version
class DefaultAppNotifier(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class EmailAppNotifier(DefaultAppNotifier):
    def send_notification(self, message: str):
        print(f"Sending email: {message}")


class UserNotifierService:
    def __init__(self, notifier: DefaultAppNotifier):
        self.notifier: DefaultAppNotifier = notifier

    def notify_user(self, message: str):
        self.notifier.send_notification(message)


# Usage
# current_notifier: DefaultAppNotifier = EmailAppNotifier()
# current_user_service = UserNotifierService(current_notifier)
# current_user_service.notify_user("Welcome!")


# Easy extendable
class MobilePushNotifier(DefaultAppNotifier):
    def __init__(self, user_name: str):
        self.user_name = user_name

    def send_notification(self, message: str):
        print(f"Push notification sent to user: {self.user_name}")
        print(f"Message: {message}")


# Usage
# new_notifier: MobilePushNotifier = MobilePushNotifier("Alex")
# new_user_service: UserNotifierService = UserNotifierService(new_notifier)
# new_user_service.notify_user(message="Hi there")


# 3. Database Connection


# Violated version
class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL Database.")

    def execute_query(self, query: str):
        print(f"Executing query: {query}")


class UserRepository:
    def __init__(self):
        self.database = MySQLDatabase()

    def get_users(self):
        self.database.connect()
        self.database.execute_query("SELECT * FROM users")


# Usage
# repo = UserRepository()
# repo.get_users()


# Refactored version
class SQLDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass


class PostgreSQLDatabase(SQLDatabase):
    def connect(self):
        print("Connecting to Postgres Database.")

    def execute_query(self, query: str):
        print(f"Executing Postgres Database query: {query}")


class LectionsRepository:
    def __init__(self, sql_database: SQLDatabase):
        self.sql_database: SQLDatabase = sql_database

    def get_lections(self):
        self.sql_database.connect()
        self.sql_database.execute_query("SELECT * FROM lections")


# Usage
postgres_db_engine: SQLDatabase = PostgreSQLDatabase()
postgres_db_lections_data: LectionsRepository = LectionsRepository(postgres_db_engine)
postgres_db_lections_data.get_lections()


# Easy extendable
class SQLiteDatabase(SQLDatabase):
    def connect(self):
        print("Connecting to SQLite Database.")

    def execute_query(self, query: str):
        print(f"Executing SQLite Database query: {query}")


sqlite_db_engine: SQLDatabase = SQLiteDatabase()
sqlite_db_lection_data: LectionsRepository = LectionsRepository(sqlite_db_engine)
sqlite_db_lection_data.get_lections()
