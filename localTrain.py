import torch
print(f"Version of torch: {torch.__version__}")
import torchvision
print(f"Version of torchvision: {torchvision.__version__}")
import torchmetrics
print(f"Version of torchmetrics: {torchmetrics.__version__}")


from config import get_config
cfg = get_config()
cfg['batch_size'] = 6
cfg['preload'] = None
cfg['num_epochs'] = 30

from train import train_model

train_model(cfg)