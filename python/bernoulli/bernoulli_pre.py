import torch
import numpy as np

from torch.autograd import Variable

sample = np.array([ 1.,  1.,  0.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  0.,  1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,  1.,  1.,  0.,  1.,  1.,
        1.,  0.,  1.,  0.,  1.,  1.,  0.,  1.,  1.,  0.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,
        0.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,  1.,  0.,  1.,
        0.,  1.,  1.,  0.,  1.,  0.,  1.,  0.,  0.,  1.,  1.,  1.,  0.,
        0.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  1.,  1.,  0.,  1.,
        0.,  1.,  1.,  1.,  1.,  1.,  0.,  1.,  0.,  0.,  1.,  1.,  1.,
        0.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,
        1.,  1.,  0.,  0.,  1.,  1.,  0.,  1.,  1.,  0.,  1.,  0.,  1.,
        1.,  1.,  1.,  0.,  1.,  0.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,
        0.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,  1.,
        1.,  1.,  1.,  0.,  1.,  1.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,
        1.,  0.,  1.,  0.,  1.])



np.mean(sample)

x = Variable(torch.from_numpy(sample)).type(torch.FloatTensor)






