**Web Scraper and Data Processor**
## Project Overview:
### This project consists of three main components:
- Fetching data from multiple URLs asynchronously.
- Processing the fetched data in parallel.
- Saving the processed data to files using worker threads.  


## Project Structure:
       scraper/
        │
        ├── main.py
        ├── fetcher.py
        ├── processor.py
        └── saver.py

1. fetcher.py - Using Asynchronous Programming to Fetch Data
2. processor.py - Using Parallel Programming to Process Data
3. saver.py - Using Worker Threads to Save Data
4. main.py - Combining Everything with Co-routines


## Running the Project
1. Install Dependencies:
    ```bash
    pip install aiohttp
    ```
2. Run the Main Script:
   ```bash
   python main.py
   ```

