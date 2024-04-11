package main

import (
 "fmt"
 "math"
 "time"
)

const (
 MAX_BUCKET_SIZE float64 = 3
 REFILL_RATE     int     = 1
)

type TokenBucket struct {
 currentBucketSize   float64
 lastRefillTimestamp int
}

func (tb *TokenBucket) allowRequest(tokens float64) bool {
 tb.refill() //refill of bucket happening at constant REFILL_RATE

 if tb.currentBucketSize >= tokens {
  tb.currentBucketSize -= tokens
  return true
 }

 return false
}

func getCurrentTimeInNanoseconds() int {
 return time.Now().Nanosecond()
}

func (tb *TokenBucket) refill() {
 nowTime := getCurrentTimeInNanoseconds()
 tokensToAdd := (nowTime - tb.lastRefillTimestamp) * REFILL_RATE / 1e9
 tb.currentBucketSize = math.Min(tb.currentBucketSize+float64(tokensToAdd), MAX_BUCKET_SIZE)
 tb.lastRefillTimestamp = nowTime
}

func main() {
 obj := TokenBucket{
  currentBucketSize:   3,
  lastRefillTimestamp: 0,
 }

 fmt.Printf("Request processed: %v\n", obj.allowRequest(1)) //true
 fmt.Printf("Request processed: %v\n", obj.allowRequest(1)) //true
 fmt.Printf("Request processed: %v\n", obj.allowRequest(1)) //true
 fmt.Printf("Request processed: %v\n", obj.allowRequest(1)) //false, request dropped
}
