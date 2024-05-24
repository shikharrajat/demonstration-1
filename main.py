# main.py
import asyncio
from fetcher import fetch_all
from processor import process_all
from saver import save_all

async def main():
    urls = [
        'http://example.com/1',
        'http://example.com/2',
        'http://example.com/3',
    ]
    
    print("Fetching data from URLs...")
    fetched_data = await fetch_all(urls)
    print("Data fetched. Processing data...")

    processed_data = process_all(fetched_data)
    print("Data processed. Saving data...")

    save_all([str(data) for data in processed_data])
    print("Data saved to files.")

# Running the main function
if __name__ == "__main__":
    asyncio.run(main())
