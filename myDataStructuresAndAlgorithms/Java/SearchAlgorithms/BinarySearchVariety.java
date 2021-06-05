package SearchAlgorithms;

public class BinarySearchVariety {

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

  public int bsearchFirstEq(int[] a, int n, int value) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
      int mid = low + ((high - low) >> 1);
      if (a[mid] == value) {
        if ((mid == 0) || (a[mid - 1] != value)) {
          return mid;
        } else {
          high = mid - 1;
        }
      } else if (a[mid] < value) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return -1;
  }

  public int bsearchLastEq(int[] a, int n, int value) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
      int mid = low + ((high - low) >> 1);
      if (a[mid] == value) {
        if ((mid == n - 1) || (a[mid + 1] != value)) {
          return mid;
        } else {
          low = mid + 1;
        }
      } else if (a[mid] < value) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return -1;
  }

  public int bsearchFirstGE(int[] a, int n, int value) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
      int mid = low + ((high - low) >> 1);
      if (a[mid] >= value) {
        if ((mid == 0) || (a[mid - 1] < value)) {
          return mid;
        } else {
          high = mid - 1;
        }
      } else {
        low = mid + 1;
      }
    }

    return -1;
  }

  public int bsearchLastLE(int[] a, int n, int value) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
      int mid = low + ((high - low) >> 1);
      if (a[mid] <= value) {
        if ((mid == n - 1) || (a[mid + 1] > value)) {
          return mid;
        } else {
          low = mid + 1;
        }
      } else {
        high = mid - 1;
      }
    }

    return -1;
  }

  public static void main(String[] args) {
    BinarySearchVariety binarySearchVariety = new BinarySearchVariety();
    // int[] arr = { 8, 11, 19, 23, 27, 33, 45, 55, 67, 98 };
    int[] arr = { 1, 3, 4, 5, 6, 8, 8, 8, 11, 18 };
    int value = 8; // need found value
    int firstGEValue = 7; // need found value
    int lastLEValue = 9;  // need found value
    int loc = -1;

    System.out.println("Binary Search, Original array is:");
    for (int a : arr) {
      System.out.print(" " + a);
    }

    System.out.println("\n\nTest Search");
    loc = binarySearchVariety.bsearch(arr, arr.length, value);
    System.out.println("The search value " + value + "'s location is " + loc);

    System.out.println("\n\nTest Search First Equal");
    loc = binarySearchVariety.bsearchFirstEq(arr, arr.length, value);
    System.out.println("The search value " + value + "'s location is " + loc);

    System.out.println("\n\nTest Search Last Equal");
    loc = binarySearchVariety.bsearchLastEq(arr, arr.length, value);
    System.out.println("The search value " + value + "'s location is " + loc);

    System.out.println("\n\nTest Search First Greater and Equal");
    loc = binarySearchVariety.bsearchFirstGE(arr, arr.length, firstGEValue);
    System.out.println("The search value " + firstGEValue + "'s location is " + loc);

    System.out.println("\n\nTest Search Last Less and Equal");
    loc = binarySearchVariety.bsearchLastLE(arr, arr.length, lastLEValue);
    System.out.println("The search value " + lastLEValue + "'s location is " + loc);
  }
}
