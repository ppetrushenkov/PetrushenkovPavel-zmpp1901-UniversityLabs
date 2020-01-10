public class Point3d {
    /** координата X **/
    private double xCoord;
    /**  координата Y **/
    private double yCoord;
    /**  координата Z **/
    private double zCoord;
    /** Конструктор инициализации **/
    public Point3d ( double x,  double y, double z) {
        xCoord = x;
        yCoord = y;
        zCoord = z;
    }
    public Point3d () {
        //Вызовите конструктор с двумя параметрами и определите источник.
        this(0, 0, 0);
    }
    /** Возвращение координаты X **/
    public double getX () {
        return xCoord;
    }
    /** Возвращение координаты Y **/
    public double getY () {
        return yCoord;
    }
    /** Возвращение координаты Z **/
    public double getZ () {
        return zCoord;
    }
    /** Установка значения координаты X. **/
    public void setX ( double val) {
        xCoord = val;
    }
    /**  Установка значения координаты Y. **/
    public void  setY ( double val) {
        yCoord = val;
    }
    /**  Установка значения координаты Z. **/
    public void  setZ ( double val) {
        zCoord = val;
    }
    /**Сравниваем точки. True значит что точки равны и наоборот**/
    public boolean compareTo(Point3d num){
        return (num.getX() == this.getX()) & (num.getY() == this.getY()) & (num.getZ() == this.getZ());
    }
    public double distanceTo(Point3d num){
        double distance = Math.sqrt(Math.pow(num.getX() - this.getX(), 2) +
                                    Math.pow(num.getY() - this.getY(), 2) +
                                    Math.pow(num.getZ() - this.getZ(), 2));
        return Math.round(distance * 100) / 100.00;
    }
}
