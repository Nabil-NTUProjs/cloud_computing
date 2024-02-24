import numpy as np
import matplotlib.pyplot as plt


# adjust as needed
ITERATEMAX = 100
C = 10
alpha = 0.1
exponent1 = 2
exponent2 = 0.5

x1 = 1
x2 = 1
alpha1 = 0
alpah2 = 0

x1_values = np.zeros(ITERATEMAX)
x2_values = np.zeros(ITERATEMAX)

for i in range(ITERATEMAX):
    #if(x1 + x2 <+ C + alpha1 + alpah2): #when alpha is large it pushes the const boundary out
    if(x1 + x2 <= C):
        #Additive increase phase
        print('Additive 1')

        alpha1 = alpha * np.power(x1,exponent1)
        alpha2 = alpha * np.log(x2 + 1)

        x1 = x1 + alpha1
        x2 = x2 + alpha2
    else:
        #Stimulate network condition(for example,congestion)
        print('Multiplicative D')
        beta1 = exponent1
        beta2 = exponent2

        x1 = x1 * beta1
        x2 = x2 * beta2

        #pause(1)

    #Store values in arrays
    x1_values[i] = x1
    x2_values[i] = x2


#Display the final values
print('Final x1: ', x1)
print('Final x2: ', x2)


# Plot the graph
plt.plot(range(ITERATEMAX), x1_values, label='x1')
plt.plot(range(ITERATEMAX), x2_values, label='x2')
plt.xlabel('Iterations')
plt.ylabel('Values')
plt.title('Values of x1 and x2 over iterations')
plt.legend()
plt.grid(True)
plt.show()

