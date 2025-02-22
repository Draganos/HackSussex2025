import java.util.HashMap;

public class Speed extends Feature{

    private final int SPEED;
    private final int LIMIT;
    private int time;

    private HashMap<Speed, Mileage> journey;

    public Speed(int carSpeed, int speedLimit, int speedVio){
        super(speedVio);
        this.SPEED = carSpeed;
        this.LIMIT = speedLimit;
        journey = new HashMap<>();
    }

    public int getSpeedingNum(){
         return this.SPEED - this.LIMIT;
    }

//    public int numOfViolations(){
//        int count = 0;
//        if (getSpeedingNum() <= 0) {
//            return ;
//        }
//        else {
//            for (int i = 0; i < super(violations); i++) {
//                return count++;
//            }
//            return count;
//        }
//    }

//    We need to create a for-each loop that checks for each journey the number of violations
//    Use a hashmap?

    public int getTime(){
        return this.time;
    }

    public void setTime(int time){
        this.time = time;
    }

    public int getAcceleration(){
        return (this.SPEED / this.time);
    }

    public void setAcceleration(){
        this.getAcceleration();
    }
}