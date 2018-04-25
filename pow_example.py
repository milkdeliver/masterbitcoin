# example of proof_of_work algorithm
# Python 3.6.4
import hashlib
import time

max_nounce = 2 ** 32 

def proof_of_work(header, difficulty_bits):
    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits)
    
    for nounce in range(max_nounce):
        hash_result= hashlib.sha256(str(str(header) + str(nounce)).encode('utf-8')).hexdigest()
        # check if this is a valid result, blow the target
        if  int(hash_result, 16) < target:
            print("Success with nounce %d" % nounce)
            print("Hash is %s" % hash_result)
            return  (hash_result, nounce)
    print ("Faild after %d (max_nounce) tries" % nounce)
    return nounce

if __name__ == '__main__':
    nounce = 0
    hash_result = ''
    # difficulty from 0 to 31 bits
    for difficulty_bits in range(32):
        difficulty = 2 ** difficulty_bits
        print("Diffculty: %ld (%d bits)" % (difficulty, difficulty_bits))
        # checkpint the current time
        start_time = time.time()

        # make a new block with which includes the hash from the previous block
        # we fake a block of transaction - just a string
        new_block = 'text block with transaction' + hash_result

        # find a valid nounce for the new block
        (hash_result, nounce) = proof_of_work(new_block, difficulty_bits)
        
        end_time = time.time()
        
        # estimate the hashes per second
        elapsed_time = end_time - start_time
        print ("Elapsed Time: %.4f seconds" % elapsed_time)

        if elapsed_time > 0:
            hash_power = float(int(nounce)/elapsed_time)
            print ("Hashing power %ld hashes per second" % hash_power)


