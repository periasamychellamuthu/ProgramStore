//$Id$
//https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
public class minimum_number_of_jumps {

	public static void main(String[] args) {
		int arr[]= {1,3,5,8,9,2,6,7,6,8,9};
//		int arr[]={1, 4, 3, 2, 6, 7};
//		int arr[]={2,3,1,1,2,4,2,0,1,1};
//		int arr[]= {2,1,0,3};
		
		int count =0,max=Integer.MIN_VALUE,maxIndex =0,i=1;
		int loop=arr[0];
		count++;
		for(i=1;(i<arr.length&&loop>0);i++) {
			System.out.println("index is"+i+"value is"+arr[i]+"length is"+arr.length+"result is "+(arr[i]-(arr.length-1-i))+"max is"+max);
			if((arr[i]-(arr.length-1-i))>max) {
				//max jump element select in a range is not based on maximum value, rather select element which occupies more element in the right side of array range.
				max=arr[i]-(arr.length-1-i);
				maxIndex = i;
			}
			loop--;
			if(loop==0 && maxIndex>0 && i<arr.length-1) {
				System.out.println("loop is "+loop+"max Index is "+maxIndex+"i is "+i);
				loop=arr[maxIndex];
				i=maxIndex;
				if(i < arr.length-1) {
					count++;
				}
				System.out.println("loop is "+loop+"max Index is "+maxIndex+"i is "+i);
				max=Integer.MIN_VALUE;
				maxIndex=-1;
			}
			System.out.println(i);
		}
		
		if(i>arr.length-1) {
			System.out.println(count);
		}else {
			System.out.println(-1);
		}

	}

}
