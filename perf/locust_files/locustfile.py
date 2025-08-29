import random

from locust import HttpUser, task, between, tag

class PublicApiUser(HttpUser):
    wait_time = between(0.5, 1.5)


    @task(3)
    @tag("list_posts")
    def list_posts(self):
        self.client.get("/posts", name="GET /posts")


    @task(2)
    @tag("get_post")
    def get_post(self):
        post_id = random.randint(1, 100)
        self.client.get(f"/posts/{post_id}", name="GET /posts/:id")


    @task(1)
    @tag("create_post")
    def create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        self.client.post("/posts", json=payload, name="POST /posts")


    def on_start(self):
    # host può anche essere impostato da CLI --host oppure da env
        if not self.host:
            self.host = "https://jsonplaceholder.typicode.com"