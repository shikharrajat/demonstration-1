# saver.py
import threading

def save_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def save_all(data_list):
    threads = []
    for i, data in enumerate(data_list):
        thread = threading.Thread(target=save_to_file, args=(f'output_{i}.txt', data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
