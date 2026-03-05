import sqlite3
import pandas as pd

def get_customer_purchase_totals():
    conn = sqlite3.connect("RetailDB.db")
    query = '''
        SELECT CustomerID, SUM(Quantity) AS TotalPurchases
        FROM Transactions
        GROUP BY CustomerID
    '''
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def get_monthly_revenue_trends():
    conn = sqlite3.connect("RetailDB.db")
    query = '''
        SELECT strftime('%Y-%m', InvoiceDate) AS Month, SUM(TotalAmount_GBP) AS Revenue
        FROM Transactions
        GROUP BY Month
        ORDER BY Month
    '''
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def get_top_5_products_by_revenue():
    conn = sqlite3.connect("RetailDB.db")
    query = '''
        SELECT StockCode, SUM(TotalAmount_GBP) AS Revenue
        FROM Transactions
        GROUP BY StockCode
        ORDER BY Revenue DESC
        LIMIT 5
    '''
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def revenue_by_country():
    conn = sqlite3.connect("RetailDB.db")
    query = '''
        SELECT Country, SUM(TotalAmount_GBP) AS Revenue
        FROM Transactions
        JOIN Customers ON Transactions.CustomerID = Customers.CustomerID
        GROUP BY Country
    '''
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result