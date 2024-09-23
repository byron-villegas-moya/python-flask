from locust import HttpUser, task, between

wait_time = between(1, 2)

class Product(HttpUser):
    @task
    def get_products(self):
        self.client.get("/products")
    
    @task
    def get_product_by_sku(self):
        self.client.get("/products/15207410")