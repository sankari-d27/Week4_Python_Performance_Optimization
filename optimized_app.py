
import random
import time


def generate_data(size=10000):
    random.seed(42)

    categories = [
        "Electronics",
        "Clothing",
        "Food",
        "Books",
        "Furniture"
    ]

    return [
        {
            "id": i,
            "category": random.choice(categories),
            "price": random.randint(100, 10000),
            "quantity": random.randint(1, 20)
        }
        for i in range(size)
    ]


def process_data(data):
    start = time.perf_counter()

    total_sales = 0
    total_price = 0

    # Initialize all categories with zero
    category_names = [
        "Electronics",
        "Clothing",
        "Food",
        "Books",
        "Furniture"
    ]

    category_sales = {
        category: 0 for category in category_names
    }

    # Efficient duplicate detection
    seen_ids = set()
    duplicates = []

    count = len(data)

    # Process all records in a single pass
    for record in data:

        price = record["price"]
        quantity = record["quantity"]
        category = record["category"]
        record_id = record["id"]

        sales = price * quantity

        # Calculate total sales
        total_sales += sales

        # Calculate total price
        total_price += price

        # Calculate category-wise sales
        category_sales[category] += sales

        # Identify duplicate IDs
        if record_id in seen_ids:
            duplicates.append(record_id)
        else:
            seen_ids.add(record_id)

    # Calculate average price
    average_price = (
        total_price / count if count else 0
    )

    result = {
        "total_sales": total_sales,
        "category_sales": category_sales,
        "duplicates": duplicates,
        "average_price": average_price
    }

    execution_time = time.perf_counter() - start

    return result, execution_time


if __name__ == "__main__":

    dataset = generate_data(10000)

    result, execution_time = process_data(dataset)

    print("\nOPTIMIZED APPLICATION")
    print("---------------------")

    print("Total Sales:", result["total_sales"])

    print("Category Sales:")
    for category, sales in result["category_sales"].items():
        print(f"{category}: {sales}")

    print("Duplicates:", len(result["duplicates"]))

    print("Average Price:", result["average_price"])

    print("Execution Time:", execution_time, "seconds")
