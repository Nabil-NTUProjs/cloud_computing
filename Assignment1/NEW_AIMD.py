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
    # Parameters
    max_cwnd = 10
    cwnd = 5
    a = 1
    b = 0.5
    
    # Iterate
    RTT_tracker = []
    for i in range(ITERATEMAX):
        cwnd = standard_AIMD(a, b, cwnd, max_cwnd, RTT_tracker)


    # Visualise
    x, y = [], []
    for idx, cwnd in enumerate(RTT_tracker):
        print(f"RTT {idx + 1}:\t", cwnd)
        x.append(idx + 1)
        y.append(cwnd)
    
    plt.plot(x, y)
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title(f"Standard AIMD")
    plt.show()

    # parameters for scalable_AIMD
    a = 0.1
    b = 0.125
    cwnd = 5
    RTT_trackerS = []
    for i in range(ITERATEMAX):
        cwnd = scalable_AIMD(a, b, cwnd, max_cwnd, RTT_trackerS)

    # Visualise
    x, y = [], []
    for idx, cwnd in enumerate(RTT_trackerS):
        print(f"RTT {idx + 1}:\t", cwnd)
        x.append(idx + 1)
        y.append(cwnd)

    plt.plot(x, y)
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title(f"Scalable AIMD")
    plt.show()

    #parameters for highspeed AIMD
    a = 0.1
    b = 0.125
    cwnd = 50
    max_cwnd = 100
    RTT_trackerH = []
    for i in range(ITERATEMAX):
        cwnd = highspeed_AIMD(a, b, cwnd, max_cwnd, RTT_trackerH)

    # Visualise
    x, y = [], []
    for idx, cwnd in enumerate(RTT_trackerH):
        print(f"RTT {idx + 1}:\t", cwnd)
        x.append(idx + 1)
        y.append(cwnd)

    plt.plot(x, y)
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title(f"HighSpeed AIMD")
    plt.show()
