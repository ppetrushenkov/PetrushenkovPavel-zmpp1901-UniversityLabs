import java.util.Scanner;

public class Lab1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String [] point1, point2, point3;
        double x, y, z, area;

        /**Вводим координаты для первой точки*/
        point1 = scan.nextLine().split(",");
        x = Double.parseDouble(point1[0]);
        y = Double.parseDouble(point1[1]);
        z = Double.parseDouble(point1[2]);
        Point3d p1 = new Point3d(x, y, z);

        /**Вводим координаты для первой точки*/
        point2 = scan.nextLine().split(",");
        x = Double.parseDouble(point2[0]);
        y = Double.parseDouble(point2[1]);
        z = Double.parseDouble(point2[2]);
        Point3d p2 = new Point3d(x, y, z);

        /**Вводим координаты для первой точки*/
        point3 = scan.nextLine().split(",");
        x = Double.parseDouble(point3[0]);
        y = Double.parseDouble(point3[1]);
        z = Double.parseDouble(point3[2]);
        Point3d p3 = new Point3d(x, y, z);

        scan.close();

        /** Сравниваем точки и если они равны, то вычисления не требуются*/
        if ((p1.compareTo(p2)) & (p1.compareTo(p3)) & p2.compareTo(p3)){
            System.out.println("Значеня равны");
        }else{
            area = computeArea(p1, p2, p3);
            System.out.println("Площадь равна " + area);
        }
    }

    public static double computeArea(Point3d p1, Point3d p2, Point3d p3){
        double a, b, c, p, area;

        a = p1.distanceTo(p2);
        b = p1.distanceTo(p3);
        c = p2.distanceTo(p3);

        p = (a + b + c) / 2;
        /** Вычисляем площадь по формуле*/
        area = Math.sqrt(p * (p - a) * (p - b) * (p - c));
        /**Возвращаем округленное значение*/
        return Math.rint(100.0 * area) / 100.0;
    }
}