package main

import (
	"fmt"
)

func merge_sort(arr []int, n int) {
	merge_sort_c(arr, 0, n-1)
}

func merge_sort_c(arr []int, start int, end int) {
	if start >= end {
		return
	}

	mid := start + ((end - start) >> 1)
	merge_sort_c(arr, start, mid)
	merge_sort_c(arr, mid+1, end)

	merge(arr, start, mid, end)
	s := fmt.Sprintf("array is %v", arr)
	fmt.Println(s)

}

func merge(arr []int, start int, mid int, end int) {
	i := start
	j := mid + 1
	k := 0

	arr_t := make([]int, end-start+1)

	for i <= mid && j <= end {
		if arr[i] <= arr[j] {
			arr_t[k] = arr[i]
			i++
		} else {
			arr_t[k] = arr[j]
			j++
		}
		k++
	}

	start_t := i
	end_t := mid
	if j <= end {
		start_t = j
		end_t = end
	}

	for start_t <= end_t {
		arr_t[k] = arr[start_t]
		k++
		start_t++
	}

	for i := 0; i < end-start+1; i++ {
		arr[start+i] = arr_t[i]
	}
}

func main() {
	// arr := [8]int{5, 3, 7, 8, 9, 1, 2, 6}
	arr := [...]int{9, 8, 7, 6, 5, 4, 3, 2, 1}
	s := fmt.Sprintf("Original array is %v", arr)
	fmt.Println(s)
	merge_sort(arr[:], len(arr))
	s = fmt.Sprintf("Sorted array is %v", arr)
	fmt.Println(s)
}
