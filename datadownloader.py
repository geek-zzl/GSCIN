import kagglehub

# Download latest version
path = kagglehub.dataset_download("elmahy/pems-dataset")

print("Path to dataset files:", path)