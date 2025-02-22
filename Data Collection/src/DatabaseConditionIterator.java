import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DatabaseConditionIterator {
    public static void main(String[] args) {
        // Database connection parameters from the PHP sample
        String url = "jdbc:mysql://sql211.infinityfree.com:3306/if0_38373169_db2025";
        String username = "if0_38373169";
        String password = "u72RmKPyhiDm ";  // Check for any trailing spaces

        // Initialize a counter variable
        int counter = 0;

        // SQL query to retrieve records (update table name as needed)
        String query = "SELECT * FROM my_table";

        // Establish connection and execute query using try-with-resources
        try (Connection conn = DriverManager.getConnection(url, username, password);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            // Iterate over each row in the result set
            while (rs.next()) {
                // Example condition: if the value in the third column is greater than 10
                int value = rs.getInt(3);
                if (value > 10) {
                    counter++;
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Output the count of records meeting the condition
        System.out.println("Number of records meeting the condition: " + counter);
    }
}
