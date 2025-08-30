from locust import HttpUser, task, SequentialTaskSet, between


# A Locust test using SequentialTaskSet executes tasks in
# a defined sequential order, unlike the default TaskSet which
# picks tasks randomly based on weighting. This is useful for
# simulating user flows where actions must occur in a specific sequence
# , such as logging in, then searching for a product, then adding it to a cart.


class MyUserBehaviour(SequentialTaskSet):

    @task
    def login(self):
        print()

    @task
    def viewproducts(self):
        pass

    @task
    def logout(self):
        pass


# The main HttpUser class that uses the SequentialTaskSet.
class demoload(HttpUser):

    host=""
    tasks = [MyUserBehaviour]
    wait_time = between(5, 9)







