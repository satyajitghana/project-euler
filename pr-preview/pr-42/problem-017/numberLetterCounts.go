package main

import (
	"fmt"
	"strings"
)

func spelling(number int) string {
	under20 := []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	tens := []string{"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}

	if number == 0 {
		return ""
	}

	if number < 20 {
		return under20[number-1]
	}

	if number < 100 {
		return tens[number/10-2] + " " + spelling(number%10)
	}

	if number < 1000 {
		if number%100 == 0 {
			return under20[number/100-1] + " hundred "
		}

		return under20[number/100-1] + " hundred and " + spelling(number%100)
	}

	if number == 1000 {
		return under20[number/1000-1] + " thousand"
	}

	return ""
}

func letterCounts(limit int) int {
	total := 0
	for i := 1; i <= limit; i++ {
		str := spelling(i)
		total += len(strings.ReplaceAll(str, " ", ""))
	}

	return total
}

func main() {
	fmt.Println(letterCounts(1000))
}
