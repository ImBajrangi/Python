import java.util.Scanner;

public class Eligible {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter age: ");
        int a =scanner.nextInt();
        if (a>=18) {
            System.out.println("eligible to vote.");
        } else {
            System.out.println("Not eligible to vote.");
        }
    }
}

public class check {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number: ");
        int a=sc.nextInt();
        if(a%7==0){
            System.out.println("Yes It Is Divisible.");
        } else {
            System.out.println("Not Divisible");
        }
        LastiIsFour(384724);
    }
    void LastiIsFour(int num) {
        String str = Integer.toString(num);
        int s = Integer.valueOf(str[-1]);
        if(s.equals(4)) {
            System.out.println("Yes, In Last Their is 4.");
        } else {
            System.out.println("No, In Last Their Is No 4.");
        }
    }
}
