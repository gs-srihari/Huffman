#!/usr/local/bin/python3
import sys
import argparse
import shutil

huff_binary = {}

def encode(input_file, output_file):
	print("encoding ", input_file, output_file)
        f = open(input_file,"r")
        a = f.read()
        f.close()
        l = [] 
        for i in a:
            l.append(i)  
        unique = set(l) 
        unique = list(unique)
        #print(unique)

        count1 = [] 
        for i in unique:
            count = 0
            for j in l:
                if j == i:
                    count = count + 1 
            count1.append(count)
            
            
        #print(count1)

        idx=[]
        for i in range(len(unique)):
            idx.append(i)
        #print(idx)


        l1 = count1.copy()    
        l1.sort()
        #print(l1)


        indxs = []
        for i1 in idx:
            val = count1[i1]
            #print(val)
            ctr = 0
            for j1 in l1:
                #print(j1)
                ctr = ctr + 1
                if val == j1:
                    if ctr not in indxs:
                        indxs.append(ctr)
            #print(indxs)

        dictionaries = {}
        for i in indxs:
            dictionaries[unique[i-1]] = count1[i-1]

        #print(dictionaries.keys())

        repetitions = 0
        repetitions = set(l1)
        repetitions = list(repetitions)
        repetitions.sort()

        #print(repetitions)

        letters = []
        count = []
        for i in repetitions:
            l1 = []
            l2 = []
            for j in dictionaries.keys():
                #print(j)
                if i == dictionaries[j]:
                    l1.append(j)
            for j in a:
                if j in l1 and j not in l2:
                    l2.append(j)
            for j in l2:
                letters.append(j)
                count.append(i)
            
            huff_binary = {}
            for i in letters:
                huff_binary[i] = ''
            
        #print(huff_binary)
            

        while len(letters) > 1:
            s1 = ''
            s2 = ''
            lts1 = []
            cnt1 = []
            lts2 = []
            cnt2 = []
            for i in range(2,len(letters)):
                lts2.append(letters[i])
                cnt2.append(count[i])
            s1 = letters[0] + letters[1]
            lts1.append(s1)
            cnt1.append(count[0] +count[1])
            s2 = letters[0] + '|' + letters[1]
            flag = 0
            for i in s2:
                if i == '|':
                    flag = 1 
                    continue 
                if flag == 0:
                    huff_binary[i] = '0' + huff_binary[i]
                if flag == 1:
                    huff_binary[i] = '1' + huff_binary[i]
            indx = 0
            for i in range(len(cnt2)):
                if cnt1[0] < cnt2[i]:
                    indx = i 
                    break 
                indx = indx + 1
            lts3 = []
            cnt3 = []
            for i in range(indx):
                lts3.append(lts2[i])
                cnt3.append(cnt2[i])
            lts3.append(lts1[0])
            cnt3.append(cnt1[0])
            for i in range(indx,len(lts2)):
                lts3.append(lts2[i])
                cnt3.append(cnt2[i])
            letters = lts3.copy()
            count = cnt3.copy()
            #print(letters)
            #print(count)

        #print(letters) 
        #print(count)
        #print(huff_binary)


        string_new = ''
        for i in a:
            string_new = string_new+huff_binary[i]

        #print(string_new)   
        f = open(output_file,”w”)
        f.write(string_new)
        f.close()


def decode(input_file, output_file):
	print("decoding ", input_file, output_file)
        f = open(input_file,"r")
        string_new = f.read()
        f.close()
        answers = huff_binary.values()
        decoded_string = ''
        encoded_alphabet = ''
        for i in string_new:
            encoded_alphabet = encoded_alphabet + i 
            if encoded_alphabet in answers:
                for j in huff_binary.keys():
                    if huff_binary[j] == encoded_alphabet:
                        decoded_string = decoded_string + j
                encoded_alphabet = ''
        f = open(output_file,"w")
        f.write(decoded_string)
        f.close()

def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
