# %%
import numpy as np
import matplotlib.pyplot as plt
mu = 0.0005
sigma = 0.01
startPrice = 5
np.random.seed(0)
returns = np.random.normal(loc = mu, scale = sigma, size = 100)
price = startPrice*(1+returns).cumprod()

# %%
plt.plot(price)
plt.show()