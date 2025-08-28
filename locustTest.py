from locust import User, task

class myTest(User):

    @task
    def startTest(self):
        print("Starting test")

    @task
    def endTest(self):
        print("Ending test")