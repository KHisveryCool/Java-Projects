
//The imports we need for random generation and writing to a text file
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;

// The program that generates strong passwords and appends all of them to passwords.txt
public class PasswordGenerator {
    public static void main(String[] args) {

        // Outer loop that runs 3 times (3 batches), as required by the assignment
        for (int i = 0; i < 3; i++) {

            try {
                // Open the file in append mode so the previous results are not overwritten
                FileWriter writer = new FileWriter("passwords.txt", true);

                // Inner loop that generates 20 passwords in this batch
                for (int j = 0; j < 20; j++) {

                    // Generate one password, then print it, and save it to the file
                    String password = genPassword();
                    System.out.println(password);
                    writer.write(password + "\n"); // write each password on a new line to reduce clutter
                }

                // Close the writer after writing all 20 passwords
                writer.close();

            } catch (IOException e) {
                // Handle any possible file I/O errors to prevent the program crashing
                System.out.println("Error writing to file.");
            }

            System.out.println("-----------"); // a separator between batches for better readability
        }
    }

    // Generates one password that follows all of the assignment rules
    public static String genPassword() {

        // The Random object that is used to generate the password length
        Random random = new Random();

        // Password will be built character-by-character and I will show later why
        String password = "";

        // Random password length from 10 to 16 (inclusive)
        int passwordLength = random.nextInt(7) + 10;

        // All of the character sets needed (alphanumeric only)
        String lowercaseletters = "abcdefghijklmnopqrstuvwxyz";
        String uppercaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String digits = "0123456789";

        // Check whether the password contains at least one of each required type ( Condition Checker )
        boolean hasLowercaseletter = false;
        boolean hasUppercaseletter = false;
        boolean hasDigits = false;

        // Build the password to the needed length (passwordLength)
        for (int i = 0; i < passwordLength; i++) {

            // nextChar stores the current chosen character before adding it to the password
            char nextChar = ' ';
            boolean validChar = false;

            // Keep selecting until the character is valid (not the same as the previous character)
            while (validChar == false) {

                // Randomly choose the character type out of the following 3 options: 0 = digit, 1 = lowercase, 2 = uppercase
                int type = (int)(3 * Math.random());

                switch (type) {
                    case 0:
                        // Choose a random digit from the digits string
                        int index = (int)(digits.length() * Math.random());
                        nextChar = digits.charAt(index);
                        break;

                    case 1:
                        // Choose a random lowercase letter from lowercase letter string
                        index = (int)(lowercaseletters.length() * Math.random());
                        nextChar = lowercaseletters.charAt(index);
                        break;

                    case 2:
                        // Choose a random uppercase letter from uppercase letter string
                        index = (int)(uppercaseletters.length() * Math.random());
                        nextChar = uppercaseletters.charAt(index);
                        break;
                }

                // Rule: no identical consecutive characters this makes sure there isnt
                if (i == 0 || nextChar != password.charAt(i - 1)) {
                    validChar = true; //if the character is not true then we move on and--
                }
            }

            // --> Add the valid character to the password
            password += nextChar;

            // Checks to see if we meet all of the conditions (a lowercase, an uppercase, and a digit) if we do then it is true
            if (nextChar >= 'a' && nextChar <= 'z') {
                hasLowercaseletter = true;
            } else if (nextChar >= 'A' && nextChar <= 'Z') {
                hasUppercaseletter = true;
            } else if (nextChar >= '0' && nextChar <= '9') {
                hasDigits = true;
            }
        }

        // Check the required rules: at least one digit, one lowercase, and one uppercase and if it is valid then we--
        if (hasDigits && hasLowercaseletter && hasUppercaseletter) {
            //--> return the password
            return password;

        } else {
            // If one of the conditions filed of any of the types, start from scratch
            return genPassword();
        }
    }
    // THE END :D
}