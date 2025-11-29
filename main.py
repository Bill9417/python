import subprocess
import device

# Call device.py and get the result
#result = subprocess.check_output(["python3", "device.py"]).decode().strip()

#if result == "cuda":
#    print("Using CUDA backend")
#else:
#    print("Using ML backend (Mac or no GPU)")

device.detect_device()
print(device.detect_device())