from ipykernel.kernelapp import IPKernelApp
from .kernel import GoKernel
IPKernelApp.launch_instance(kernel_class=GoKernel)
