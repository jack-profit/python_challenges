import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100) # chuang jian 100 ge fen bu zai 0 dao 1 de zhi
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('shi yan lou')

ax.plot(x, x ** (1/8), 'b--', label=r'$y = x^{1/8}$') # x zhou, y zhou, blue xu xian, biao qian
ax.plot(x, x ** 8, 'r--', label=r'$y = x^{8}$') # x zhou, y zhou, red xu xian, biao qian

ax.plot(x, x ** (1/2), 'r.', label=r'$y = x^{1/2}$') # x zhou, y zhou, red dian xian, biao qian
ax.plot(x, x ** 2, 'b.', label=r'$y = x^{2}$') # x zhou, y zhou, blue dian xian,biao qian

ax.plot(x, x, 'g-', label=r'$y = x$') # x zhou, y zhou, green shi xian, biao qian

ax.legend()
ax.axis([0, 1, 0, 1])
plt.show()
