import time
wait_time=1
attempt=0
max_retries=5
while(attempt<=max_retries):
    print(f"Retry {attempt}: Waiting {wait_time} seconds...")
    time.sleep(wait_time)  
    wait_time *= 2  
    attempt += 1  

print("Max retries reached. Stopping.")