#Library Source:
#https://pypi.org/project/manufacturing/

#pip install manufacturing

import numpy as np
import manufacturing

data = np.random.normal(0,1, size=30)
print(data)

manufacturing.ppk_plot(data, lower_specification_limit=-2, upper_specification_limit=2)

manufacturing.control_plot(data, upper_control_limit=7.0, lower_control_limit=-7.0)

manufacturing.suggest_specification_limits(data,sigma_level=6)

manufacturing.ppk_plot(data, lower_specification_limit=-7.8, upper_specification_limit=8.6)
