import threading

total = 0
lock = threading.Lock()

def update_total(amount):
    """
    Updates the total by the given amount

    we no longer need the try/finally as the context manager
    that is provided by the with statement does all of that for us
    """
    global total
    with lock:
        total += amount
    print (total)

if __name__ == '__main__':
    for i in range(10):
        my_thread = threading.Thread(
            target=update_total, args=(5,))
        my_thread.start()
