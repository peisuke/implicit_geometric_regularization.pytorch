import torch
import torch.nn as nn
import torch.nn.functional as F

class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.l1 = nn.Linear(2, 128)
        self.l2 = nn.Linear(128, 128)
        self.l3 = nn.Linear(128, 126)
        self.l4 = nn.Linear(128, 128)
        self.l5 = nn.Linear(128, 1)

    def forward(self, x):
        h = F.softplus(self.l1(x))
        h = F.softplus(self.l2(h))
        h = F.softplus(self.l3(h))
        h = torch.cat((h, x), axis=1)
        h = F.softplus(self.l4(h))
        h = self.l5(h)
        return h