
import random
import time


def generate_data(size=10000):
    random.seed(42)

    data = []

    categories = ["Electronics", "Clothing", "Food", "Books", "Furniture"]

    for i in range(size):
        record = {
            "id": i,
            "category": random.choice(categories),
            "price": random.randint(100, 10000),
            "quantity": random.randint(1, 20)
        }

        data.append(record)

    return data


def calculate_total_sales(data):
    total = 0

    for record in data:
        total += record["price"] * record["quantity"]

    return total


def calculate_category_sales(data):
    categories = ["Electronics", "Clothing", "Food",
                  "Books", "Furniture"]

    result = {}

    for category in categories:
        total = 0

        # Inefficient repeated scanning
        for record in data:
            if record["category"] == category:
                total += record["price"] * record["quantity"]

        result[category] = total

    return result


def find_duplicates(data):
    duplicates = []

    # Inefficient nested loop
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i]["id"] == data[j]["id"]:
                duplicates.append(data[i]["id"])

    return duplicates


def calculate_average(data):
    total = 0

    for record in data:
        total += record["price"]

    return total / len(data) if data else 0


def process_data(data):
    start = time.perf_counter()

    total_sales = calculate_total_sales(data)
    category_sales = calculate_category_sales(data)
    duplicates = find_duplicates(data)
    average_price = calculate_average(data)

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

    print("\nORIGINAL APPLICATION")
    print("--------------------")
    print("Total Sales:", result["total_sales"])
    print("Category Sales:", result["category_sales"])
    print("Duplicates:", len(result["duplicates"]))
    print("Average Price:", result["average_price"])
    print("Execution Time:", execution_time, "seconds")
