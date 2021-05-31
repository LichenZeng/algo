public class BinarySearch {

  public int bsearch(int[] a, int n, int value) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
      //   int mid = (low + high) / 2;
      int mid = low + ((high - low) >> 1);
      if (a[mid] == value) {
        return mid;
      } else if (a[mid] < value) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return -1;
  }

  // binary search base on recursion method
  public int bsearch_recurion(int[] a, int n, int val) {
    return bsearchInternally(a, 0, n - 1, val);
  }

  private int bsearchInternally(int[] a, int low, int high, int value) {
    if (low > high) return -1;

    int mid = low + ((high - low) >> 1);
    if (a[mid] == value) {
      return mid;
    } else if (a[mid] < value) {
      return bsearchInternally(a, mid + 1, high, value);
    } else {
      return bsearchInternally(a, low, mid - 1, value);
    }
  }

  public static void main(String[] args) {
    BinarySearch binarySearch = new BinarySearch();
    int[] arr = { 8, 11, 19, 23, 27, 33, 45, 55, 67, 98 };
    int value = 33; // need found value
    int loc = -1;

    System.out.println("Binary Search, Original array is:");
    for (int a : arr) {
      System.out.print(" " + a);
    }

    System.out.println("\n\nTest Search");
    loc = binarySearch.bsearch(arr, arr.length, value);
    System.out.println("The search value " + value + "'s location is " + loc);

    System.out.println("\n\nTest Search recursion");
    loc = binarySearch.bsearch_recurion(arr, arr.length, value);
    System.out.println("The search value " + value + "'s location is " + loc);
  }
}
