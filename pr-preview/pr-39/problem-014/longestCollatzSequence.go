package main

import "fmt"

type longestCollatzSequenceStruct struct {
	start int
	total int
}

func collatz(number int) int {
	if number%2 == 0 {
		return number / 2
	}

	return number*3 + 1
}

func collatzSequence(start int) []int {
	var sequence []int

	sequence = append(sequence, start)

	for start != 1 {
		start = collatz(start)
		sequence = append(sequence, start)
	}

	return sequence
}

func longestCollatzSequence(limit int) {
	var longest longestCollatzSequenceStruct

	for i := 1; i <= limit; i++ {
		sequenceTemp := collatzSequence(i)
		sequenceLengthTemp := len(sequenceTemp)

		if longest.total < sequenceLengthTemp {
			longest.start = i
			longest.total = sequenceLengthTemp
		}
	}

	fmt.Println(longest.start)
}

func main() {
	longestCollatzSequence(1000000)
}
