import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy             as np

train_nums = [
    [1, 1, 1,
     1, 0, 1, 
     1, 0, 1, 
     1, 0, 1, 
     1, 1, 1
    ],
    [0, 0, 1, 
     0, 0, 1, 
     0, 0, 1, 
     0, 0, 1, 
     0, 0, 1
    ],
    [1, 1, 1, 
     0, 0, 1, 
     1, 1, 1, 
     1, 0, 0, 
     1, 1, 1
    ],
    [1, 1, 1, 
     0, 0, 1, 
     1, 1, 1,
     0, 0, 1,
     1, 1, 1
    ],
    [1, 0, 1,
     1, 0, 1,
     1, 1, 1,
     0, 0, 1, 
     0, 0, 1
    ],
    [1, 1, 1,
     1, 0, 0,
     1, 1, 1,
     0, 0, 1, 
     1, 1, 1
    ],
    [1, 1, 1,
     1, 0, 0,
     1, 1, 1, 
     1, 0, 1, 
     1, 1, 1
    ],
    [1, 1, 1,
     0, 0, 1, 
     0, 0, 1, 
     0, 0, 1, 
     0, 0, 1
    ],
    [1, 1, 1,
     1, 0, 1, 
     1, 1, 1, 
     1, 0, 1, 
     1, 1, 1
    ],
    [1, 1, 1,
     1, 0, 1, 
     1, 1, 1, 
     0, 0, 1, 
     1, 1, 1
    ]
]

defected_fives = [[
1, 1, 1,
1, 0, 0,
1, 1, 1,
0, 0, 0,
1, 1, 1
],
[
1, 1, 1,
1, 0, 0,
0, 1, 0,
0, 0, 1,
1, 1, 1
],
[
1, 1, 1,
1, 0, 0,
0, 1, 1,
0, 0, 1,
1, 1, 1
],
[
1, 1, 0,
1, 0, 0,
1, 1, 1,
0, 0, 1,
1, 1, 1
],
[
1, 1, 0,
1, 0, 0,
1, 1, 1,
0, 0, 1,
0, 1, 1
],
[
1, 1, 1,
1, 0, 0,
1, 0, 1,
0, 0, 1,
1, 1, 1
]]


def printWeights(w, title='карта получившихся весов'):
    dat = np.array(w).reshape((-1,3))
    fig = plt.figure()
    pc = plt.imshow(dat,cmap=mpl.cm.get_cmap('RdYlGn')) 
    plt.colorbar(pc)
    plt.title(title)
    
cmap = mpl.colors.ListedColormap(['white','black'], 'indexed')

def printNum(num, title):
    dat = np.array(num).reshape((-1,3))
    fig = plt.figure()
    pc = plt.imshow(dat,cmap=cmap) 
    plt.title(title)

def printNums(nums):
    dat = np.concatenate(tuple(
            np.concatenate(tuple((
                np.array(num).reshape((-1,3)),
                np.zeros((len(num) // 3,1))
            )),1)
                for num in nums
             ),1)
    fig = plt.figure()
    pc = plt.imshow(dat,cmap=cmap)

sample_good_weight   = [1, 2, 1, 3, 0, -11, 1, 2, 1, -11, 0, 2, 2, 2, 1]
sample_middle_weight = [0, 1, 0, 3, 0, -8, 0, 1, 0, -4, 0, 1, 1, 1, 0]    
sample_bad_weight = [1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1]  
