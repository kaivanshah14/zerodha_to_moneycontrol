import csv
import sys
from datetime import datetime

# Check for command-line arguments
if len(sys.argv) != 3:
    print("Usage: python transform_csv.py <input_file> <output_file>")
    sys.exit(1)

# Input and output file paths from command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Define the two headers for the output file
header1 = [
    "ISIN Code",
    "Enter Full/Partial Stock Name",
    "Date",
    "Transaction Type (Enter Either Buy or Sell)",
    "Exchange",
    "Qty",
    "Purchase/Sell price per share",
    "Total Amount",
    "Total Charges (Brokerage +Other charges)",
    "Net Amount",
    "Note",
    "Order Number",
    "Transaction Number",
    "Contract Note Number",
    "Brokerage",
    "Other Charges (All Charges other than brokerage charges)",
    "Service Tax/GST",
    "STT",
    "Exchange Charges",
    "Stamp Duty",
    "SEBI Charges"
]

header2 = [
    "",  # Empty cell
    "Mandatory", "Mandatory", "Mandatory", "Mandatory", "Mandatory", 
    "Mandatory", "Optional", "Optional", "Optional", "Optional", 
    "Optional", "Optional", "Optional", "Optional", "Optional", 
    "Optional", "Optional", "Optional", "Optional", "Optional"
]

# Mapping input columns to output columns
column_mapping = {
    "isin": "ISIN Code",
    "symbol": "Enter Full/Partial Stock Name",
    "trade_date": "Date",
    "trade_type": "Transaction Type (Enter Either Buy or Sell)",
    "exchange": "Exchange",
    "quantity": "Qty",
    "price": "Purchase/Sell price per share",
    "order_id": "Order Number",
    "trade_id": "Transaction Number"
}

# Function to transform the date format
def transform_date(input_date):
    try:
        # Parse the input date (DD-MM-YY)
        parsed_date = datetime.strptime(input_date, "%d-%m-%y")
        # Format to desired output (DD/MM/YYYY)
        return parsed_date.strftime("%m/%d/%Y")
    except ValueError:
        # Return the input date if parsing fails
        return input_date

# Read the input file and write to the output file
try:
    with open(input_file, mode="r", encoding="utf-8") as infile, open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        reader = csv.DictReader(infile, delimiter=",")  # Assuming comma-separated input
        writer = csv.writer(outfile)
        
        # Debug: Print the detected headers
        print("Detected headers:", reader.fieldnames)
        
        # Write headers
        writer.writerow(header1)
        writer.writerow(header2)
        
        # Transform and write data rows
        for row in reader:
            # Transform the date
            transformed_date = transform_date(row.get("trade_date", ""))
            
            output_row = [
                row.get("isin", ""),
                row.get("symbol", ""),
                transformed_date,  # Transformed date
                row.get("trade_type", ""),
                row.get("exchange", ""),
                row.get("quantity", ""),
                row.get("price", ""),
                "",  # Total Amount (calculation can be added here)
                "",  # Total Charges (not in input, leave empty or calculate)
                "",  # Net Amount (not in input, leave empty or calculate)
                "",  # Note (not in input, leave empty)
                row.get("order_id", ""),
                row.get("trade_id", ""),
                "",  # Contract Note Number (not in input, leave empty)
                "",  # Brokerage (not in input, leave empty)
                "",  # Other Charges (not in input, leave empty)
                "",  # Service Tax/GST (not in input, leave empty)
                "",  # STT (not in input, leave empty)
                "",  # Exchange Charges (not in input, leave empty)
                "",  # Stamp Duty (not in input, leave empty)
                "",  # SEBI Charges (not in input, leave empty)
            ]
            
            # Debug: Print the constructed output row
            print("Writing row:", output_row)
            writer.writerow(output_row)

    print(f"Transformation complete. Output written to {output_file}")

except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
