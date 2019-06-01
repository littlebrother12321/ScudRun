import simpy

# An Electric Car class
class Car(object):

    # Initializes with the environment from simpy
    def __init__(self, env):
        self.env = env
        # Call the run() function everytime an instance is created
        self.action = env.process(self.run())

    def run(self):
        while True:
            print("Start parking and charging at %d" % self.env.now)
            charge_duration = 5
            # We yield the process that process() returns
            # to wait for it to finish
            yield self.env.process(self.charge(charge_duration))

            # The charge process is finished and we can drive again
            print("Start driving at %d" % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)


env = simpy.Environment()
car = Car(env)
env.run(until=30)
