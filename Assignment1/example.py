import math
import matplotlib.pyplot as plt

def AIMD(a:int=1, b:float=0.5, cwnd:int=0, RTT_tracker:list=[], max_window=10)->list:
    """This function mimics the Additive Increase and Multiplicative Decrease Mechanism in TCP Congestion Control.
 
    Parameters
    ----------
    a: int-type
    This constant controls the rate of Additive Increase. This optimises the efficiency of the network.
    
    b: float-type
    This constant controls the rate of Multiplicative Decrease. This optimises the fairness of the network.
    This value is between 0 (exclusive) and alpha (exclusive).
    
    With these two parameters, the network system converges to optimal network conditions where the fairness line intersects with the 
    efficiency line.
    
    cwnd: int-type
    This denotes the current window size.
    
    data_packet: tuple-type
    This represents the data packet to be transferred through the network.
    
    RTT_tracker: list-type
    This tracks the RTT to cwnd size.
    
    Returns
    -------
    cwnd load
    """
    _, status = data_packet
    
    if status == 'Transfer':
        cwnd += a
    else:
        cwnd = cwnd * b
        
    RTT_tracker.append(cwnd)
    
    return cwnd

def scalable_AIMD(a:int=1, b:float=0.125, cwnd:int=10, data_packet:tuple=(None, "Dropped"), RTT_trackerS:list=[])->list:

    _, status = data_packet
    
    if status == 'Transfer':
        cwnd = cwnd + (0.1 * cwnd)
    else:
        cwnd = cwnd * b
        
    RTT_trackerS.append(cwnd)
    
    return cwnd

if __name__ == "__main__":
    # Set Up for Data
    data_packets = [(x, "Transfer") if x % 10 != 0 else (x, "Dropped") for x in range(1, 101)]
    
    # for idx, cwnd in data_packets:
    #     print(f"data_packet {idx}:\t", cwnd)

    ITERATEMAX = 100
    # Parameters
    max_cwnd = 10
    cwnd = 0
    a = 1
    b = 0.5
    
    # Iterate
    RTT_tracker = []
    for i in range(ITERATEMAX):
        cwnd = AIMD(a, b, cwnd, RTT_tracker, max_cwnd)

    cwnd = 10
    b = 0.125
    # scalable AIMD
    RTT_trackerS = []
    for data_packet in data_packets:
        cwnd = scalable_AIMD(a, b, cwnd, data_packet, RTT_trackerS)

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

    # Visualise for Scalable
    i, j = [], []
    for idx, cwnd in enumerate(RTT_trackerS):
        print(f"RTT {idx + 1}:\t", cwnd)
        i.append(idx + 1)
        j.append(cwnd)
    
    plt.plot(i, j)
    plt.xlabel("RTT")
    plt.ylabel("CWND")
    plt.title(f"Scalable AIMD")
    plt.show()