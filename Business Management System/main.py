from users import Admin
from ledger import Ledger
from documents import Invoice
from inventory import InventoryManager
from reports import ReportFactory

# Create Admin
admin = Admin("Jani", "jani@biz.com")
print("Logged in as:", admin)

# Ledger System
ledger = Ledger()
invoice1 = Invoice("Acme Corp", [("Design", 1200), ("Development", 3000)])
invoice2 = Invoice("Beta Ltd", [("Consulting", 1500)])
ledger.add_entry(invoice1)
ledger.add_entry(invoice2)

# Inventory System
inventory = InventoryManager()
inventory.add_product("Laptop", 10)
inventory.add_product("Monitor", 3)

# Generate CSV Report
report = ReportFactory.create("csv", ledger.entries)
print("\n--- Ledger Report (CSV) ---")
print(report.render())

# Low Stock Alerts
print("\n--- Low Stock Items ---")
for item in inventory.low_stock_items():
    print(item)

# Ledger Total
print("\n--- Total Ledger Amount ---")
print("$", ledger.total())