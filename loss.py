# Arun Srinivasan V K (002839500), and Abhinav Anil (002889398)
# 4/24/2024
# Purpose - This file contains the loss function

import torch.nn as nn
from torchvision.models import vgg19
import config


# custom VGG Loss module
class VGGLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.vgg = vgg19(pretrained=True).features[:35].eval().to(config.DEVICE)

        for param in self.vgg.parameters():
            param.requires_grad = False

        self.loss = nn.MSELoss()

    def forward(self, input, target):
        vgg_input_features = self.vgg(input)
        vgg_target_features = self.vgg(target)
        return self.loss(vgg_input_features, vgg_target_features)