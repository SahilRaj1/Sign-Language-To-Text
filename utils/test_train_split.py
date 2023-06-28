import os
import splitfolders

"""
    Spliting the dataset in the directory itself
"""
def test_train_split(data_dir):
    input_file = data_dir
    output_file = data_dir
    splitfolders.ratio(input_file, output=output_file, seed=38, ratio=(.8, .2), group_prefix=None)

__all__ = ['test_train_split']
