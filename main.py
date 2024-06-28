from datetime import datetime

def time_delta(t1, t2):
    # Define the format of the input timestamps
    fmt = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the timestamps into datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    # Calculate the absolute difference in seconds
    delta = abs(int((dt1 - dt2).total_seconds()))
    
    return delta



if __name__ == '__main__':
    t = int(input().strip())  # Number of test cases
    
    for _ in range(t):
        t1 = input().strip()  # First timestamp
        t2 = input().strip()  # Second timestamp
        
        # Calculate the time difference
        result = time_delta(t1, t2)
        
        # Print the result for this test case
        print(result)


