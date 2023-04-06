import random

def generate(data):
    
    # randomize work done by g
    g = ["constant", "linear", "quadratic", "exponential", "logarithmitic"]
    gIndex = random.randint(0, 5)
    data["params"]["c"] = g[gIndex]

    # randomize n stopping condition in base case
    n = random.randint(0, 10)
    data["params"]["d"] = n

    # randomize input size in recursive case
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    data["params"]["a"] = f'N / {a}'
    data["params"]['b'] = f'N / {b}'
    
    # randomize number of recursive calls
    num_recursive = random.randint(1, 4)
    

    # randomize print statements
    num_prints = random.randint(0, 2)


    