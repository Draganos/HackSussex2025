public class Mileage extends Feature{

    private int distance;
    private int trips;

    public Mileage(int tripDist, int numOfTrips, int speedVio){
        super(speedVio);
        this.distance = tripDist;
        this.trips = numOfTrips;
    }

    public int violationsPerMile(){
        return distance / getViolations();
    }
}