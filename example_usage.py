from client import SqlOptimizerClient

def main():
    client = SqlOptimizerClient()
    res = client.optimize_query(query='SELECT * FROM users')
    print(f"Result for optimized_sql: {res['optimized_sql']}")

if __name__ == "__main__":
    main()
