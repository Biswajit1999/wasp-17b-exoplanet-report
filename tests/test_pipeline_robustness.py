import unittest
import numpy as np
from scripts.pipeline_robustness import paired_offset, delete_block_offsets

class TestPipelineRobustness(unittest.TestCase):
    def test_equal_error_offset(self):
        self.assertAlmostEqual(paired_offset([3,4,5],[1,2,3],[1]*3,[1]*3)[0],2)
    def test_positive_correlation_reduces_error(self):
        a=[2,3,4];b=[1,2,3];e=[1]*3
        self.assertLess(paired_offset(a,b,e,e,.8)[1],paired_offset(a,b,e,e,0)[1])
    def test_block_stability(self):
        r=delete_block_offsets([3]*6,[1]*6,[1]*6,[1]*6,2)
        np.testing.assert_allclose(r[:,0],2)
        self.assertEqual(r.shape,(3,2))
    def test_bad_input(self):
        with self.assertRaises(ValueError): paired_offset([1,2],[1,2],[1,0],[1,1])
        with self.assertRaises(ValueError): delete_block_offsets([1,2],[1,2],[1,1],[1,1],1)
