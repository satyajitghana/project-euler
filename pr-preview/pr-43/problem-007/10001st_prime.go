package main

import (
	"fmt"
	"math/big"
)

func firstNPrime(n int) int {
	var nPrime int = 0

	for i := 2; n != 0; i++ {
		if big.NewInt(int64(i)).ProbablyPrime(0) {
			nPrime = i
			n--
		}
	}

	return nPrime
}

func main() {
	fmt.Println(firstNPrime(10001))
}
