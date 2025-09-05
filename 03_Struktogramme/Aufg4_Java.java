public class Main {
    public static void main(String[] args) {
        helloworld();
    }

    private static void helloworld() {
        System.out.println("Hello world!");
    }

    private static void aufg_1() {
        int s = 0;
        for (int i = 1; i <= 100; i++) {
            s += i;
        }
        System.out.println(s);
    }

    private static void aufg_2() {
        int i = 1;
        do{
            System.out.println(i);
            if(i == 39) {
                i = 61;
            } else {
                i++;
            }
        }while(i <= 100);
    }

    private static void quadratzahlen(int n) {
        for (int i = 1; i <= n ; i++) {
            System.out.println(i*i);
        }
    }
}