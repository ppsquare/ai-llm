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

# xsum data sets

# features: ['gem_id', 'gem_parent_id', 'xsum_id', 'document', 'target', 'references'] datasets list

# 1. train , num_rows: 23206
# 2. validation, num_rows: 1117
# 3. test , num_rows: 1166
# 4. challenge_train_sample , num_rows: 500
# 5. challenge_validation_sample, num_rows: 500
# 6. challenge_test_backtranslation, num_rows: 500
# 7. challenge_test_bfp_02, num_rows: 500
# 8. challenge_test_bfp_05, num_rows: 500
# 9. challenge_test_nopunc, num_rows: 500
# 10. challenge_test_covid, num_rows: 401

import datasets
data = datasets.load_dataset('GEM/xsum')
data
