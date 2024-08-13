import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]
N = 50

net = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)

def status_updates(data):
    global net 
    
    new_net = net.copy()
    
    for i in range(N):
        for j in range(N):
            total = (net[i, (j-1)%N] + net[i, (j+1)%N] +
            net[(i-1)%N, j] + net[(i+1)%N, j] +
            net[(i-1)%N, (j-1)%N] + net[(i-1)%N, (j+1)%N] +
            net[(i+1)%N, (j-1)%N] + net[(i+1)%N, (j+1)%N])/255
            
            if net[i, j] == ON:
                if total < 2 or total > 3:
                    new_net[i, j] = OFF
                elif total == 3 or total == 2:
                    new_net[i, j] = ON
            
    noise = np.random.choice(vals, N * N, p=[0.20, 0.80]).reshape(N, N)
    new_net = np.maximum(new_net, noise)
    
    net = new_net
    
    mat.set_data(net)
    return [mat]

fig, ax = plt.subplots()

mat = ax.matshow(net)

ani = animation.FuncAnimation(fig, status_updates, interval=50, save_count=50)

plt.show()