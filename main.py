#1 bar() fnction
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(1,10,10)
#we use plt.bar for this type and we need fill size in height or width
plt.bar(x, height=12,width=12)
plt.show()


#2 barh() function
import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(2,30,10)
#we use plt.barh for this type and we need fill size in height or width
plt.barh(x, height=5,width=.01)
plt.show()

#The both are different with: bar() function is vertical and  barh() function is horizontal bar
#We always must fill size in height or width


#3 and we can use both functions at once time and with color

import matplotlib.pyplot as plt
import numpy as np

x = [12,323,4,35,4]
y = [12,54,87,347,8]

plt.bar(x,y, color = "red")
plt.barh(x,y, color = "hotpink")
plt.show()



