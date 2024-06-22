import os
import random
import string

def generate_pages(directory, num_unique_pages):
    os.makedirs(directory, exist_ok=True)
    for i in range(num_unique_pages):
        page_content = ''.join(random.choices(string.ascii_lowercase, k=10))
        with open(os.path.join(directory, f"{i}.pag"), 'w') as f:
            f.write(page_content)

def generate_page_requests(num_requests, num_unique_pages):
    return [random.randint(0, num_unique_pages - 1) for _ in range(num_requests)]