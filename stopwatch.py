from datetime import datetime

class stopwatch():
    def __init__(self):
        self.__start_time = datetime.now()
        self.__end_time = ""

    def stop(self):
        self.__end_time = datetime.now()

    def total(self):
        return self.__end_time - self.__start_time

    def __str__(self):
        return str(self.total())



# begin= input("Press 1 to start")

# while begin != "1":
#     begin = input("Press 1 to start")

# else: 
#     start = datetime.now()
#     end = input("Press 2 to stop the clock")
#     while end != "2":
#         final = input("Press 2 to stop the clock")

#     else: 
#         end = datetime.now()

# total_time = end - start
# print(total_time)

