# Script to import Zerodha Stocks to Money Control

## Step by Step-by-step guide on How to import stocks from Zerodha to Money Control

### Step 1: Importing Stocks from Zerodha
1. Go to https://console.zerodha.com and log in with your Kite account
2. Navigate to https://console.zerodha.com/reports/tradebook and select the required date range. The segment will be "Equity." Then, generate the trade book.
3. Once the trade book is generated, download it in .csv format. The download option and file extension are both present beside the "Search" button in the Tradebook report.

### Step 2: Transform Zerodha Tradebook report to Money Control format
1. Now that you have generated the Tradebook report from Zerodha, give the file a suitable name. Example: "input.csv"
2. Open Windows Terminal/Windows CMD or any terminal. Navigate to the location where your Zerodha Tradebook is present.
3. Make sure you have installed Python 3.10 or higher version. You can check your Python installation or your version using the following command: ```python --version```
4. Copy the above code and save it with the filename as "transform_csv.py" in the same location where your Zerodha Tradebook is present.
5. Run the following command: ```python transform_csv.py input.csv output.csv```
6. This will generate the file in Money Control's format with the name "output.csv". We need to upload this file at [moneycontro;.com](https://www.moneycontrol.com/)

### Step 3: Adding stocks to Money Control
1. Navigate to https://www.moneycontrol.com/portfolio-management/portfolio-investment-dashboard/stock and log in to your account.
2. Click on "Add Transaction" under My Accounts tab.
3. Click on "Stock/ETF" and select the "File Upload" option.
4. Under Step 3, under Upload Data click on "Browse" and select your output.csv
5. Click on the "Submit" button
6. You should now see a preview of all the stocks you want to add from Zerodha to Money Control.
7. Verify the information and make changes as necessary. At the end click on "Add Transaction" to add all the above transactions. 

**That's it! You have now added your Zerodha Stocks to Money Control. This way you can keep your portfolio in sync between both platforms. 🥂** 

Happy Trading! Happy Coding! 😊
