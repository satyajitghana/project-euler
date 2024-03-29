# Longest Collatz sequence

## Go Solution

```Go
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
```

OUTPUT

```txt
837799
```

## C++ Solution

```c++
#include <iostream>
#include <numeric>
#include <unordered_map>

int main(int argc, char* argv[]) {
    u_int64_t limit = 1'000'000;  // 1 million
    // u_int64_t limit = 1'000;

    std::unordered_map<u_int64_t, u_int64_t> collatz_lengths;
    collatz_lengths[1] = 1;

    for (u_int64_t i = 1; i <= limit; i++) {
        if (collatz_lengths.find(i) != collatz_lengths.end()) {
            // found in collatz lengths
            // nothing to do
            continue;
        } else {
            u_int64_t collatz_num = i;
            u_int64_t collatz_length = 0;

            while (collatz_num != 1) {
                // std::cout << "collatz_num: " << collatz_num << ", collatz_length: " << collatz_length << std::endl;

                if (collatz_num % 2 == 0) {
                    collatz_num /= 2;
                } else {
                    collatz_num = 3 * collatz_num + 1;
                }

                collatz_length += 1;

                // check again if its in map
                if (collatz_lengths.find(collatz_num) != collatz_lengths.end()) {
                    // found it, just add the length from the map
                    collatz_length += collatz_lengths[collatz_num];
                    break;
                }
            }

            collatz_lengths[i] = collatz_length;
        }
    }

    // for (auto i : collatz_lengths) {
    //     std::cout << "num: " << i.first << ", length: " << i.second << std::endl;
    // }

    std::pair<uint64_t, u_int64_t> longest_collatz(1, 1);

    for (auto i : collatz_lengths) {
        if (i.second > longest_collatz.second) {
            longest_collatz.second = i.second;
            longest_collatz.first = i.first;
        }
    }

    std::cout << "longest length: " << longest_collatz.second << ", num: " << longest_collatz.first << std::endl;

    return EXIT_SUCCESS;
}
```


OUTPUT


```text
longest length: 525, num: 837799
```
