# from transformers.integrations import version
# from datasets import load_dataset
# from transformers import pipeline

# xsum_dataset = load_dataset (
#     "xsum",
#     version="1.2.0",
#     #cache_dir=DA.paths.datasets
#     cache_dir="https://huggingface.co/datasets/xsum"
# )
# xsum_dataset


import datasets
data = datasets.load_dataset('GEM/xsum')
data
