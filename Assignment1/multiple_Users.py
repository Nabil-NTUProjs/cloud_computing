import math
import matplotlib.pyplot as plt

def standard_AIMD(a, b, cwnd, maxWindowSize, RTT_tracker:list=[])->list:
    if cwnd < maxWindowSize:
        cwnd += a
    else:
        cwnd = cwnd * b
    
    RTT_tracker.append(cwnd)

    return cwnd

def scalable_AIMD(a, b, cwnd, maxWindowSize, RTT_tracker:list=[])->list:
    if cwnd < maxWindowSize:
        cwnd = cwnd + a * cwnd
    else:
        cwnd = cwnd * b
    
    RTT_tracker.append(cwnd)

    return cwnd

def highspeed_AIMD(a, b, cwnd, maxWindowSize, RTT_tracker:list=[])->list:
    # Define the thresholds for adjusting a and b
    low_thresh = 38
    high_thresh = 83

    # Adjust a and b based on cwnd
    if cwnd < low_thresh:
        a = 1
        b = 0.5
    elif cwnd > high_thresh:
        a = 10
        b = 0.1
    else:
        a = 0.01 * cwnd
        b = 0.01 * cwnd

    # Standard AIMD algorithm
    if cwnd < maxWindowSize:
        cwnd += a
    else:
        cwnd = cwnd * b

    RTT_tracker.append(cwnd)

    return cwnd


def simulate(users, algo, a, b, max_cwnd, ITERATEMAX):
    RTT_trackers = [[] for _ in range(users)]
    cwnds = [5 for _ in range(users)]

    for i in range(ITERATEMAX):
        for user in range(users):
            cwnds[user] = algo(a, b, cwnds[user], max_cwnd, RTT_trackers[user])

    return RTT_trackers

if __name__ == "__main__":
    ITERATEMAX = 100
    max_cwnd = 10
    users = 10  # number of users

    # Standard AIMD
    a = 1
    b = 0.5
    RTT_trackers = simulate(users, standard_AIMD, a, b, max_cwnd, ITERATEMAX)
    for user in range(users):
        plt.plot(range(1, ITERATEMAX + 1), RTT_trackers[user])
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title("Standard AIMD")
    plt.show()

    # Scalable AIMD
    a = 0.1
    b = 0.125
    RTT_trackers = simulate(users, scalable_AIMD, a, b, max_cwnd, ITERATEMAX)
    for user in range(users):
        plt.plot(range(1, ITERATEMAX + 1), RTT_trackers[user])
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title("Scalable AIMD")
    plt.show()

    # Highspeed AIMD
    a = 0.1
    b = 0.125
    max_cwnd = 100
    RTT_trackers = simulate(users, highspeed_AIMD, a, b, max_cwnd, ITERATEMAX)
    for user in range(users):
        plt.plot(range(1, ITERATEMAX + 1), RTT_trackers[user])
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title("HighSpeed AIMD")
    plt.show()
