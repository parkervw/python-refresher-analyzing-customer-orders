customers = [
	"Ava Mitchell",
	"Noah Parker",
	"Mia Thompson",
	"Liam Carter",
	"Sophia Reed",
	"Ethan Brooks",
	"Olivia Hayes",
	"Lucas Bennett",
	"Emma Wilson",
	"James Torres",
	"Isabella Chen",
]

transaction_logs = [
	("Ava Mitchell", "Wireless Earbuds", 79.99, "Electronics"),
	("Ava Mitchell", "Graphic Tee", 18.5, "Clothing"),
	("Ava Mitchell", "Desk Lamp", 24.99, "Home Essentials"),
	("Noah Parker", "Running Shoes", 64.95, "Clothing"),
	("Noah Parker", "Coffee Maker", 49.0, "Home Essentials"),
	("Mia Thompson", "Smartwatch", 129.0, "Electronics"),
	("Mia Thompson", "Laptop Sleeve", 22.0, "Electronics"),
	("Liam Carter", "Denim Jacket", 58.0, "Clothing"),
	("Liam Carter", "Cotton Sheets", 39.5, "Home Essentials"),
	("Sophia Reed", "Blender", 46.75, "Home Essentials"),
	("Sophia Reed", "Graphic Tee", 19.0, "Clothing"),
	("Ethan Brooks", "Wireless Earbuds", 79.99, "Electronics"),
	("Ethan Brooks", "Running Shoes", 69.5, "Clothing"),
	("Olivia Hayes", "Coffee Maker", 55.25, "Home Essentials"),
	("Olivia Hayes", "Smartwatch", 135.0, "Electronics"),
	("Lucas Bennett", "Laptop Sleeve", 25.5, "Electronics"),
	("Lucas Bennett", "Denim Jacket", 62.0, "Clothing"),
	("Emma Wilson", "Phone Cable", 12.99, "Electronics"),
	("Emma Wilson", "Notebook", 8.5, "Home Essentials"),
	("James Torres", "Graphic Tee", 19.99, "Clothing"),
	("Isabella Chen", "Water Bottle", 15.75, "Home Essentials"),
	("Isabella Chen", "Phone Cable", 11.99, "Electronics"),
]

products_ordered = {
	"Ava Mitchell": ["Wireless Earbuds", "Graphic Tee", "Desk Lamp"],
	"Noah Parker": ["Running Shoes", "Coffee Maker"],
	"Mia Thompson": ["Smartwatch", "Laptop Sleeve"],
	"Liam Carter": ["Denim Jacket", "Cotton Sheets"],
	"Sophia Reed": ["Blender", "Graphic Tee"],
	"Ethan Brooks": ["Wireless Earbuds", "Running Shoes"],
	"Olivia Hayes": ["Coffee Maker", "Smartwatch"],
	"Lucas Bennett": ["Laptop Sleeve", "Denim Jacket"],
	"Emma Wilson": ["Phone Cable", "Notebook"],
	"James Torres": ["Graphic Tee"],
	"Isabella Chen": ["Water Bottle", "Phone Cable"],
}

product_categories = {
	"Wireless Earbuds": "Electronics",
	"Smartwatch": "Electronics",
	"Laptop Sleeve": "Electronics",
	"Phone Cable": "Electronics",
	"Denim Jacket": "Clothing",
	"Running Shoes": "Clothing",
	"Graphic Tee": "Clothing",
	"Blender": "Home Essentials",
	"Coffee Maker": "Home Essentials",
	"Cotton Sheets": "Home Essentials",
	"Desk Lamp": "Home Essentials",
	"Notebook": "Home Essentials",
	"Water Bottle": "Home Essentials",
}

# Task 2: Classify products by category
# Create a set of unique product categories
unique_categories = set(category for category in product_categories.values())

# Display all available product categories
print("=" * 50)
print("UNIQUE PRODUCT CATEGORIES")
print("=" * 50)
print(f"All available product categories: {unique_categories}")
print()

# Task 3: Analyze customer orders
# Initialize dictionary to track total spending
customer_total_spent = {}
for customer in customers:
	customer_total_spent[customer] = 0

# Calculate total spending per customer
for transaction in transaction_logs:
	transaction_amount = transaction[2]
	customer = transaction[0]
	customer_total_spent[customer] += transaction_amount

# Classify customers based on total spending
customer_classification = {}
for customer in customers:
	total = customer_total_spent[customer]
	if total > 100:
		customer_classification[customer] = "high-value buyer"
	elif total < 50:
		customer_classification[customer] = "low-value buyer"
	else:
		customer_classification[customer] = "moderate buyer"

# Count the number of customers in each classification category
classification_counts = {
	"high-value buyer": 0,
	"low-value buyer": 0,
	"moderate buyer": 0
}
for customer, classification in customer_classification.items():
	classification_counts[classification] += 1
	
# Display classifications and # of customer is each category
print("=" * 50)
print("CUSTOMER CLASSIFICATIONS & COUNTS")
print("=" * 50)
for classification, count in classification_counts.items():
    print(f"There were {count} customers classified as {classification}.")
print()

# Task 4: Generate business insights
# Calculate total revenue per product category
product_category_revenues = {}
for category in unique_categories:
	product_category_revenues[category] = 0
	for transaction in transaction_logs:
		transaction_amount = transaction[2]
		transaction_category = transaction[3]
		if transaction_category == category:
			product_category_revenues[category] += transaction_amount

# Extract unique products from all orders using a set
unique_products = set(transaction[1] for transaction in transaction_logs)

# Build a set of products within the "Electronics" category
electronic_products = {product for product, category in product_categories.items() if category == "Electronics"}

# Find all customers who purchased electronics (using set intersection)
electronics_customers = [
	customer
	for customer, product_list in products_ordered.items()
	if set(product_list) & electronic_products
]

# Identify the top three highest-spending customers
top_three_customers = sorted(
	customer_total_spent.items(),
	key=lambda item: item[1],
	reverse=True
)[:3]

# Find most frequently purchased products
product_purchase_count = {}
for transaction in transaction_logs:
	product = transaction[1]
	product_purchase_count[product] = product_purchase_count.get(product, 0) + 1

# Sort by frequency (most purchased first)
most_frequent_products = sorted(
	product_purchase_count.items(),
	key=lambda item: item[1],
	reverse=True
)

# Display business insights
print("=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)
print("Total Revenue by Category:")
for category, revenue in product_category_revenues.items():
	print(f"  {category}: ${revenue:.2f}")

print(f"\nUnique Products Sold: {len(unique_products)}")
print(f"Products: {', '.join(sorted(unique_products))}")

print(f"\nMost Frequently Purchased Products:")
for i, (product, count) in enumerate(most_frequent_products[:5], 1):
	print(f"  {i}. {product:<20} - purchased {count} time(s)")

print(f"\nCustomers Who Purchased Electronics ({len(electronics_customers)}):")
for customer in electronics_customers:
	print(f"  - {customer}")

print("\nTop 3 Highest-Spending Customers:")
for i, (customer, total) in enumerate(top_three_customers, 1):
	print(f"  {i}. {customer}: ${total:.2f}")
print()

# Task 5: Organize and display data
# Find customers who purchased from multiple categories
multi_category_customers = []
for customer in customers:
	categories_purchased = set()
	for product in products_ordered[customer]:
		categories_purchased.add(product_categories[product])
	if len(categories_purchased) > 1:
		multi_category_customers.append(customer)

# Identify customers who bought both electronics and clothing
common_category_customers = []
categories_required = {"Electronics", "Clothing"}
for customer in customers:
	categories_purchased = set()
	for product in products_ordered[customer]:
		categories_purchased.add(product_categories[product])
	if categories_required <= categories_purchased:  # Is categories_required a subset of categories_purchased
		common_category_customers.append(customer)

# Display organized data
print("=" * 50)
print("ORGANIZED DATA & SET OPERATIONS")
print("=" * 50)
print("Customer Spending Summary:")
for customer in customers:
	total = customer_total_spent[customer]
	classification = customer_classification[customer]
	print(f"  {customer:<20} ${total:>8.2f} - {classification}")

print(f"\nCustomers Who Purchased from Multiple Categories ({len(multi_category_customers)}):")
for customer in multi_category_customers:
	categories = set(product_categories[product] for product in products_ordered[customer])
	print(f"  - {customer:<15}: {', '.join(sorted(categories))}")

print(f"\nCustomers Who Purchased Both Electronics AND Clothing ({len(common_category_customers)}):")
for customer in common_category_customers:
	print(f"  - {customer}")
print()

