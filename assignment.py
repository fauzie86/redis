import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Sample product dictionary
sample_product = {
    'id': 'product5578',
    'quantity': 80,
    'price': 15.85
}

def update_product(redis_conn, product, quantity_increment, new_price):
    # Create a pipeline
    pipe = redis_conn.pipeline()

    # Increment quantity using hincrby
    pipe.hincrby(product['id'], 'quantity', quantity_increment)

    # Set new price using hset
    pipe.hset(product['id'], 'price', new_price)

    # Execute the pipeline
    pipe.execute()

# Example usage
update_product(r, sample_product, quantity_increment=7, new_price=14.99)

# Retrieve and display the updated values
updated_values = r.hgetall(sample_product['id'])
print("Updated Product Details:", updated_values)