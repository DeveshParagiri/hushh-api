import requests
import concurrent.futures
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to run.")
        return result
    return wrapper








URL = "https://hushh-preferences-ca2467be7055.herokuapp.com/fashion"

headers = {
    'id': 'test@hush1one.com',
    'authentication': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'
}

def send_request(_):
    response = requests.get(URL, headers=headers)
    # Handle the response here if needed
    print(response.text)

@time_decorator
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(send_request, range(5))

main()




