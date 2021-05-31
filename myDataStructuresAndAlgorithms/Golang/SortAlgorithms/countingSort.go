package main

import (
	"fmt"
)

func countingSort(arr []int, n int) {
	if n <= 1 {
		return
	}

	max := arr[0]
	for i := 1; i < n; i++ {
		if max < arr[i] {
			max = arr[i]
		}
	}

	c := make([]int, max+1)
	for i := 0; i < max+1; i++ {
		c[i] = 0
	}

	for i := 0; i < n; i++ {
		c[arr[i]]++
	}

	for i := 1; i < max+1; i++ {
		c[i] += c[i-1]
	}

	arr_t := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		index := c[arr[i]] - 1
		arr_t[index] = arr[i]
		c[arr[i]]--
	}

	for i := 0; i < n; i++ {
		arr[i] = arr_t[i]
	}
}

func main() {
	arr := [...]int{9, 8, 7, 6, 5, 4, 3, 2, 1}
	// arr := [8]int{5, 3, 7, 8, 9, 1, 2, 6}
	s := fmt.Sprintf("Original array is %v", arr)
	fmt.Println(s)
	countingSort(arr[:], len(arr))
	s = fmt.Sprintf("Sorted array is %v", arr)
	fmt.Println(s)
}
