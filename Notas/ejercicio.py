import numpy as np 

ts={3.3,3.2,3.0,}

t_mean=np.mean(ts)

t_std=np.std(ts)

print(f"t_mean:{round(t_mean,1)}\nt_std:{round(t_std,1)}")
