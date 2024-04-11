#----------Algorithm for API rate limiting - Token Bucket Algorithm-----------------#

import time

def getCurrentTimeInNanoseconds() -> int:
    return time.time_ns()

class constants:
    MAX_BUCKET_SIZE: float = 3
    REFILL_RATE: int = 1

class TokenBucket(object):
    def __init__(self,CURRENT_BUCKET_SIZE,LAST_REFILL_TIMESTAMP):
        self.curr_bucket_size = CURRENT_BUCKET_SIZE
        self.last_refill_timestamp = LAST_REFILL_TIMESTAMP

    def allowRequests(self,tokens:float) -> bool:
        # refill of bucket happening at constant REFILL_RATE
        self.refill()

        if self.curr_bucket_size >= tokens:
            self.curr_bucket_size -= tokens
            return True
        
        return False
    
    def refill(self):
        now_time = getCurrentTimeInNanoseconds()
        tokensToAdd = (now_time - self.last_refill_timestamp) * constants.REFILL_RATE / pow(10,9)
        self.curr_bucket_size = min(self.curr_bucket_size + float(tokensToAdd),constants.MAX_BUCKET_SIZE)
        self.last_refill_timestamp = now_time


if __name__ == '__main__':
    obj = TokenBucket(CURRENT_BUCKET_SIZE=3,
                      LAST_REFILL_TIMESTAMP=0)
    print (f"Request Processed: {obj.allowRequests(1)}\n")
    print (f"Request Processed: {obj.allowRequests(1)}\n")
    print (f"Request Processed: {obj.allowRequests(1)}\n")
    print (f"Request Processed: {obj.allowRequests(1)}\n")