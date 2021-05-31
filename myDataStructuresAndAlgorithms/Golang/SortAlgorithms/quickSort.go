package main

import (
	"fmt"
)

func quick_sort(arr []int, n int) {
	quick_sort_c(arr, 0, n-1)
}

func quick_sort_c(arr []int, start int, end int) {
	if start >= end {
		return
	}

	pivot := partition(arr, start, end)
	quick_sort_c(arr, start, pivot-1)
	quick_sort_c(arr, pivot+1, end)

	s := fmt.Sprintf("array is %v", arr)
	fmt.Println(s)

}

func partition(arr []int, start int, end int) int {
	pivot := arr[end]
	i := start
	for j := start; j < end; j++ {
		if arr[j] < pivot {
			arr[i], arr[j] = arr[j], arr[i]
			i++
		}
	}
	arr[i], arr[end] = arr[end], arr[i]
	return i
}

func main() {
	// arr := [8]int{5, 3, 7, 8, 9, 1, 2, 6}
	// arr := [...]int{9, 8, 7, 6, 5, 4, 3, 2, 1}
	arr := [...]int{4, 3, 2, 1, 9, 8, 7, 6, 5}
	s := fmt.Sprintf("Original array is %v", arr)
	fmt.Println(s)
	quick_sort(arr[:], len(arr))
	s = fmt.Sprintf("Sorted array is %v", arr)
	fmt.Println(s)
}
