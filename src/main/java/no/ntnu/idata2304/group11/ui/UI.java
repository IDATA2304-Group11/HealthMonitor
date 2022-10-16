package no.ntnu.idata2304.group11.ui;

import static no.ntnu.idata2304.group11.ui.Appearance.ANSI_GREEN;
import static no.ntnu.idata2304.group11.ui.Appearance.ANSI_YELLOW;
import java.util.Scanner;

/**
 * Class represents the text-based user interface.
 */
public class UI {

  private final Scanner scanner;
  private static final int SEE_STATISTICS = 1;
  private static final int DRAW_GRAPH = 2;
  //Add more cases

  /**
   * Create an object of Interface.
   */
  public UI() {
    this.scanner = new Scanner(System.in);
  }

  /**
   * Main method of class. Starts the text-based user interface.
   */
  public void start() {
    boolean finished = false;

    while (!finished) {
      int menuChoice = this.showMenu();

      switch (menuChoice) {

        case 1:
          break;

        case 2:
          break;

        case 3:
          break;

        case 4:
          System.out.println("Thanks for using HealthMonitor.");
          finished = true;
      }
    }
  }

  /**
   * Prints to the interface.
   *
   * @return the menuchoice from the user.
   */
  private int showMenu() {
    System.out.println();
    System.out.println(ANSI_YELLOW + "        Welcome to HealthMonitor! ");
    System.out.println(ANSI_GREEN + "Please enter any number of the options below:");
    System.out.println();
    System.out.println("1. See statistics");
    System.out.println("4. Quit");
    System.out.println();

    int menuChoice;

    if (scanner.hasNextInt()) {
      menuChoice = scanner.nextInt();
    } else {
      menuChoice = 0;
    }
    return menuChoice;
  }
}