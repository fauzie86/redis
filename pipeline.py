import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

def rate_limiter(user_id, limit):
    # Create a pipeline
    pipe = r.pipeline()

    # Get the current count of requests
    pipe.get(user_id)

    # Increment the count if below our limit
    pipe.incr(user_id)

    # Execute pipeline
    result = pipe.execute()

    # Check current count, return True if within limit, False otherwise
    current_count = int(result[0] or 0)
    if current_count <= limit:
        return True
    else:
        return False

# Test the rate limiter
user_id = 'user123'
limit = 5

for _ in range(7):
    if rate_limiter(user_id, limit):
        print("Request allowed")
    else:
        print("Request denied")

    
    
