# test_hooks.py

import os
import pdb


def sample_func():
    print("Hello World")
    pdb.set_trace()  # Should be caught by debug-statements
    x = "Hello 'world'"  # Should be fixed by double-quote-string-fixer
    return x

# The test function below should be flagged by name-tests-test
def sample_test_func():
    assert sample_func() == "Hello 'world'"
