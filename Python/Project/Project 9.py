class Robot:
    def __init__(self, name):
        self.name = name
        self.battery_level = 100  # Battery level in percentage

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def perform_task(self, task):
        if self.battery_level > 0:
            print(f"{self.name} is performing the task: {task}")
            self.battery_level -= 10  # Decrease battery level after performing a task
        else:
            print(f"{self.name} has no battery left to perform the task.")
    
    def recharge(self):
        print(f"{self.name} is recharging...")
        self.battery_level = 100  # Recharge battery to full

Tom = Robot("Tom")
Jerry = Robot("Jerry")

print(Tom.name)
Tom.greet()
Tom.perform_task("cooking")
Tom.recharge()
print(Tom.battery_level)
Tom.recharge()
print(Jerry.name)
Jerry.greet()
print(Jerry.battery_level)
print(Jerry.perform_task("cleaning"))
Jerry.recharge()