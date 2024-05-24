# processor.py
import concurrent.futures

def process_data(data):
    # Example processing: counting words
    return len(data.split())

def process_all(data_list):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_data, data_list))
    return results
