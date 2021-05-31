package main

import (
	"fmt"
)

func insertSort(arr []int, n int) {
	if n <= 1 {
		return
	}

	for i := 1; i < n; i++ {
		value := arr[i]
		j := i - 1
		for ; j >= 0; j-- {
			if arr[j] > value {
				arr[j+1] = arr[j]
			} else {
				break
			}
		}
		arr[j+1] = value
	}
}

func main() {
	arr := [8]int{5, 3, 7, 8, 9, 1, 2, 6}
	s := fmt.Sprintf("Original array is %v", arr)
	fmt.Println(s)
	insertSort(arr[:], 8)
	s = fmt.Sprintf("Sorted array is %v", arr)
	fmt.Println(s)
}
