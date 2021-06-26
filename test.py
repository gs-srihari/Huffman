# Test functions goes here
import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
	# write all your tests here
	# function name should be prefixed with 'test'
    def test_encode(self):
        infile = 'input1.txt'
        outfile = 'output1.txt'
        encode(infile,outfile)
        outfile = open(outfile,'r')
        output = outfile.readlines()
        print(output[0])
        encoded_output = "1011001011000101011011"
        validity = (output[0] == encoded_output)
        self.assertTrue(validity)
    def test_decode(self):
        infile = 'input2.txt'
        outfile = 'output2.txt'
        decode(infile,outfile)
        outfile = open(outfile,'r')
        output = outfile.readlines()
        decoded_output = "ab abc cab\n"
        validity = (output[0] == decoded_ouput)
        self.assertTrue(validity)
		


if __name__ == '__main__':
    unittest.main()
