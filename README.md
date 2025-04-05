# unittest-with-llm-data

This project demonstrates how to generate test data for domain model tests using a Large Language Model (LLM). It includes an example of a domain model (`Electronics`) and uses an LLM to generate test data for unit tests.

## Features

- **Domain Model**: Defines an `Electronics` model with the following fields:
  - `model` (string): The name of the product.
  - `brand` (string): The brand of the product.
  - `category` (string): The category of the product.
  - `price` (float): Must be greater than 0.
  - `release_date` (string): Must be in ISO 8601 format and in the past.
- **LLM Integration**: Uses an LLM to generate a list of electronic products with realistic data.
- **Unit Testing**: Includes unit tests to validate the generated data, such as:
  - Ensuring `price` is positive.
  - Validating `release_date` is in the past.
  - Checking that `model` names are unique.

## Requirements

- `pydantic` library
- `unittest` (built-in)
- `mirascope` library for LLM integration

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/unittest-with-llm-data.git
   cd unittest-with-llm-data
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the unit tests to validate the generated data:
```bash
python main.py
```

## Project Structure

```
.
├── main.py         # Main script with domain model, LLM integration, and unit tests
├── README.md       # Project documentation
├── requirements.txt # Dependencies for the project
└── __pycache__/    # Compiled Python files (ignored by Git)
```

## Example

The `list_electronics` function generates a list of electronic products using an LLM. The unit tests validate that the generated data conforms to the `Electronics` model. For example:

- **Input**: `list_electronics(5)`
- **Output**: A list of 5 electronic products with fields like `model`, `brand`, `category`, `price`, and `release_date`.


