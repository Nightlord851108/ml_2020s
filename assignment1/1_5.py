import random

if __name__ == '__main__':
    max = 0
    max_p = 0
    max_theta = 0
    for i in range(201):
        theta = 0.0
        while theta == 0.0:
            theta = random.random()
        p = theta * theta * (1-theta) * (1-theta) * theta
        if (p > max_p):
            max_p = p
            max_theta = theta

    print(max_theta)
