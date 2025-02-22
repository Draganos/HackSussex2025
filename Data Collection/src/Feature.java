import java.util.HashMap;

public class Feature {

    public int violations;
    public int distance;

    public Feature(int speedVio){
        this.violations = speedVio;
    }

    public int getViolations(){
        return this.violations;
    }

    public void setViolations(int speedVio){
        this.violations = speedVio;
    }
}