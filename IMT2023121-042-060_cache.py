"""
Cache Simulator

This script simulates a cache hierarchy and calculates the hit and miss rates for different cache sizes, block sizes, and number of ways.

Parameters:
    input_path (str): Path to the input file containing the addresses to be accessed.
    output_path (str): Path to the output file where the cache access results will be written.

Returns:
    None
"""
#importing necessary libraries
import matplotlib.pyplot as graph
import math
#[cachesize(bytes), no_of_ways, address_length(bits), block_size(bytes), cache_lines, cache_line_size(bytes), offset(bits), index(bits), tag(bits)]

def part(input_path, output_path):
    #class to simulate a cache with given specifications
    class Cache:
        def __init__(self, size=1024*1024, block_size=4 , ways=4):
            self.ways = ways
            self.block_size = block_size
            self.num_of_lines = size//(self.ways*self.block_size) 
            self.lines = [{f"way{i+1}": -1 for i in range(self.ways)} for _ in range(self.num_of_lines)]
            #lines is a list as cache lines and each line is a dictionary representing ways
            #the dictionary contains tag as the index and the age as the value
            self.hit = 0
            self.miss = 0

        #calculates all the parameters and bits for each field
        def identifiers(self, address):
            offset_size = int(math.log(self.block_size,2))
            index_size = int(math.log(self.num_of_lines,2))
            left1 = 32 - offset_size
            left2 = left1 - index_size
            #handle the offset
            if offset_size > 0:
                offset = int(address[left1:32], 2)
            else:
                offset = 0
            #handle the index
            if index_size > 0:
                index = int(address[left2:left1], 2)
            else:
                index = 0
            tag = address[0:left2]
            return offset, index, tag
        
        #this fuction can also be used in miss to increment all the 
        def updateageint(self, index, tag):
        #find the way (key) where the tag is located
            for way in self.lines[index]:
                if (self.lines[index][way] == tag):
                    #update the ages(increment age for all other used ways)
                    for other_way in self.lines[index]:
                        if (self.lines[index][other_way] != -1):
                            self.lines[index][other_way] += 1
                    #set the age of the hit tag to 0(most recently used)
                    self.lines[index][way] = 0
                    break
            
        #function that accesses the cache for each address
        def cache_access(self, address):
            offset, index, tag = self.identifiers(address)
            #check if hit or miss
            if (tag in self.lines[index]):
                self.hit += 1
                self.updateageint(index,tag)#update all age bits
                return "Hit"
            else:
                self.miss += 1
                replaced = False
                for way in self.lines[index]:
                    if (self.lines[index][way] == -1):
                        old_key = way
                        new_key = tag
                        self.lines[index][new_key] = self.lines[index].pop(old_key)
                        self.lines[index][new_key] = 0
                        self.updateageint(index, new_key)
                        replaced = True
                        break
                #if no block is free, some address has to be vacated
                if(replaced==False):
                    max_key = max(self.lines[index], key=self.lines[index].get)
                    new_key = tag
                    self.lines[index][new_key] = self.lines[index].pop(max_key)
                    self.lines[index][new_key] = 0
                    self.updateageint(index, new_key)
                return "Miss"

    #handles input files and loads them in a list
    addresses = []
    with open(input_path, 'r') as input_file:
        for line in input_file:
            parts = line.split()
            if len(parts) == 3:
                address_hexa = parts[1]
                #converting hexadecimal to binary
                #string manipulation to make it valid 32 bit binary
                address_binary = bin(int(address_hexa, 16))[2:].zfill(32)
                addresses.append(address_binary)

#----------------------------------------------Part A----------------------------------------------#
    cache_a = Cache()#everything is constant
    with open(output_path, 'w') as output_file:
        for address in addresses:
            result = cache_a.cache_access(address)
            output_file.write(f"{address} results in a {result}\n")

    print(f"Cache trace results were written to {output_path}")
    print("Total MISSES:", cache_a.miss)
    print("Total HITS:", cache_a.hit)
#----------------------------------------------Part B----------------------------------------------#    
    #cache size is varying
    cache_sizes = [128, 256, 512, 1024, 2048, 4096]
    miss_rates = []
    hit_rates = []
    for cache_size in cache_sizes:
        cache_b= Cache(cache_size*1024)
        for address in addresses:
            result = cache_b.cache_access(address)

        total_accesses = cache_b.hit + cache_b.miss
        hit_rate = cache_b.hit / total_accesses
        hit_rates.append(hit_rate)
        miss_rate = cache_b.miss / total_accesses
        miss_rates.append(miss_rate)
        print(f"Cache Size: {cache_size} KB, Miss Rate: {miss_rate:.4f}, Hit Rate: {hit_rate:.4f}")
    #potting the results
    graph.figure(figsize=(10, 6))
    graph.plot(cache_sizes, miss_rates, marker='o', label='Miss Rate')
    graph.title('Miss Rate vs Cache Size')
    graph.xlabel('Cache Size (KB)')
    graph.ylabel('Miss Rate')
    graph.grid(True)
    graph.legend()
    graph.show()
#----------------------------------------------Part C----------------------------------------------#
    #list of block sizes to test (in bytes)
    block_sizes = [1, 2, 4, 8, 16, 32, 64, 128]
    miss_rates = []
    for block_size in block_sizes:
        cache_c = Cache(1024*1024, block_size)
        for address in addresses:
            result = cache_c.cache_access(address)

        total_accesses = cache_c.hit + cache_c.miss
        miss_rate = cache_c.miss / total_accesses
        miss_rates.append(miss_rate)
        print(f"Block Size: {block_size} bytes, Miss Rate: {miss_rate:.4f}")
    #plotting the results
    graph.figure(figsize=(10, 6))
    graph.plot(block_sizes, miss_rates, marker='o', label='Miss Rate')
    graph.title('Miss Rate vs Block Size (Cache Size 1024 KB)')
    graph.xlabel('Block Size (bytes)')
    graph.ylabel('Miss Rate')
    graph.grid(True)
    graph.legend()
    graph.show()
#----------------------------------------------Part D----------------------------------------------#
    #the number of ways/accociativity is varying
    no_of_ways = [1, 2, 4, 8, 16, 32, 64]
    hit_rates = []
    for ways in no_of_ways:
        cache_d = Cache(1024*1024, 4, ways)
        for address in addresses:
            result = cache_d.cache_access(address)

        total_accesses = cache_d.hit + cache_d.miss
        hit_rate = cache_d.hit / total_accesses
        hit_rates.append(hit_rate)
        print(f"Number of Ways: {ways}, Hit Rate: {hit_rate:.4f}")
    #plotting the results
    graph.figure(figsize=(10, 6))
    graph.plot(no_of_ways, hit_rates, marker='o', label='Hit Rate')
    graph.title('Hit Rate vs Number Of Ways (Cache Size 1024 KB)')
    graph.xlabel('Number Of Ways')
    graph.ylabel('Hit Rate')
    graph.grid(True)
    graph.legend()
    graph.show()

#calling the fuction by giving appropriate input and output destinations
part('C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/traces/gcc.trace', 'C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/output_gcc.txt')
part('C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/traces/gzip.trace', 'C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/output_gzip.txt')
part('C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/traces/mcf.trace', 'C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/output_mcf.txt')
part('C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/traces/swim.trace', 'C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/output_swim.txt')
part('C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/traces/twolf.trace', 'C:/Users/Harsh/OneDrive/Desktop/Codes/ca_caches_assignment/output_twolf.txt')