package main

import (
	"fmt"
)

func bubbleSort(arr []int, n int) {
	if n <= 1 {
		return
	}

	for i := 0; i < n; i++ {
		flag := false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				tmp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = tmp
				flag = true
			}
		}
		if !flag {
			break
		}
	}
}

func main() {
	arr := [8]int{5, 3, 7, 8, 9, 1, 2, 6}
	s := fmt.Sprintf("Original array is %v", arr)
	fmt.Println(s)
	bubbleSort(arr[:], 8)
	s = fmt.Sprintf("Sorted array is %v", arr)
	fmt.Println(s)
}
