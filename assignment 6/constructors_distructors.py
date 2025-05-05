class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.") 


print("Creating logger1...")
logger1 = Logger()

print("Creating logger2 inside a block...")
def create_logger():
    logger2 = Logger()

create_logger() 

print("Exiting the program...")