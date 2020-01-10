public class Palindrome {
    public static void main(String[] args) {
        String a = "HEOEH";
        System.out.println(isPalindrome(a));
    }

    public static String reverseString(String s) {
        StringBuilder pal = new StringBuilder();
        for (int i = s.length()-1; i >= 0; i--){
            pal.append(s.charAt(i));
        }
        return pal.toString();
    }

    public static boolean isPalindrome(String s) {
        return s.equals(reverseString(s));
    }
}
