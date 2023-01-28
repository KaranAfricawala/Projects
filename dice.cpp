#include <iostream>
#include <time.h>

using namespace std;


// MARK: Enumeration including all faces of a Die
enum diePattern { Fish, Shrimp, Crab, Chicken, Coin, Barrel };


// MARK: Definition of the class - Die
class Die {

private:
    diePattern dieValue[3];// An array to store 3 dices pattern after each shake

public:
    Die() {
        dieValue[0] = dieValue[1] = dieValue[2] = Fish; // Constructor used to assign all die as Fish;
    }

    void shake();

    diePattern* get();
};


// MARK: Definition of all the methods in the class - Die

// TASK: To generate random die-pattern on each die
void Die::shake() {
    srand((unsigned int)time(NULL));// To initialize the pseudo-random number generator by passing the argument seed.
    dieValue[0] = static_cast<diePattern>(rand() % 6);
    dieValue[1] = static_cast<diePattern>(rand() % 6);
    dieValue[2] = static_cast<diePattern>(rand() % 6);
}

// TASK: To return a pointer to the private variable dieValue
diePattern* Die::get() {
    return dieValue;
}


// MARK: Main function

int main() {

    string menu = "\n          Million Dollar Game summer 2020       \n"
        "                     ==============        \n"
        "0.Help(display rules for this game)\n"
        "1.Enter the total amount of money you bring in the casino for gambling\n"
        "2.Roll the dice and then place your bet here(Max. is $600, Min. is $10)\n"
        "3.Check win or lose for this round only\n"
        "4.Display your gambling results\n"
        "9.Quit\n";

    string help = "\n-------------RULES------------\n"
        "1.Initial cash for this game is specified by player.\n"
        "2.Maximum bet for each game is  $600.\n"
        "3.Minimum bet for each game is  $10.\n"
        "4.Three dice are used per game.\n"
        "5.Player can place his or her bet on any one of those six face-patterns of the die for each game.\n"
        "6.The winning prize is based on how many matched dice have been found:\n"
        "      (A)If two matched dice have been found, then the prize is 3x.\n"
        "      (B)If three matched dice have been found, then the prize is 9x.\n"
        "      (C)If no matched die has been found, then the player loses his or her bet for this game-session.\n";

    string betOptions = "0.Fish\n"
        "1.Shrimp\n"
        "2.Crab\n"
        "3.Chicken\n"
        "4.Coin\n"
        "5.Barrel\n";


    // MARK: Variable Definitions - All variables are initialized so as to not run into unexpected behaviour

    int gamesPlayed = 0;// To track number of games played
    int gamesWon = 0;// To track number of games won
    int amount = -1;// To track total amount person has
    int flag = 0;// To track whether person has already set the total money he came with
    int betChoice = -1;// To track option chosen by person in each game
    int betAmount = 0;// To track amount bet by person in each game
    int choice = -1;// To track menu options
    int currentGameStatus = -1;// To track whether person has lost or won the current game
    Die game;// To create a game with 3 dices
    diePattern* result;// To track the 3 faces of dices after each shake.


    // MARK: Executuon of game

    while (true) {
        cout << menu;
        cout << "\nEnter your choice : ";
        cin >> choice;

        if (choice == 0) {
            cout << help;
        }

        if (choice == 1) {
            if (!flag) {
                cout << " Enter the amount to be gambled with : ";
                cin >> amount;
                if (amount < 10) {
                    int quitOption = 1;
                    cout << "You do not have enough money!!Do you wish to quit?\n0.No\n1.Yes\n";
                    cin >> quitOption;
                    if (quitOption) {
                        choice = 9;
                    }
                    else {
                        choice = 1;
                    }
                }
                else {
                    flag = 1;
                }
            }
            else {
                cout << "You have already set the amount to be gambled with!";
            }
        }

        if (choice == 2) {
            if (flag) {
                cout << "Enter the amount you want to bet : ";
                cin >> betAmount;
                if (betAmount >= 10 && betAmount <= 600 && betAmount <= amount) {
                    cout << betOptions;
                    betChoice = -1;
                    cout << "Enter you bet choice : ";
                    cin >> betChoice;
                    game.shake();
                    int matchedDiceCount = 0;
                    if (betChoice <= 5 && betChoice >= 0) {
                        result = game.get();
                        for (int i = 1; i <= 3; i++) {
                            if (result[i] == betChoice) {
                                matchedDiceCount++;
                            }
                        }
                        if (matchedDiceCount == 0) {
                            amount = amount - betAmount;
                            currentGameStatus = 0;
                        }
                        else if (matchedDiceCount == 1) {
                            amount = amount + (betAmount * 2);
                            currentGameStatus = 1;
                            gamesWon++;
                        }
                        else if (matchedDiceCount == 2) {
                            amount = amount + (betAmount * 3);
                            gamesWon++;
                            currentGameStatus = 1;
                        }
                        else if (matchedDiceCount == 3) {
                            amount = amount + (betAmount * 9);
                            gamesWon++;
                            currentGameStatus = 1;
                        }
                        gamesPlayed++;
                    }
                }
                else {
                    cout << "Your bet amount is erroneous!";
                }
            }
            else {
                cout << "You have not yet entered the total money you brought to casino.";
            }
        }

        if (choice == 3) {
            if (betChoice <= 5 && betChoice >= 0) {
                if (currentGameStatus) {
                    cout << "Win!";
                }
                else {
                    cout << "Lose!";
                }
            }
            else {
                cout << "You have not yet placed the bet or chose the wrong option!";
            }
        }

        if (choice == 4) {
            cout << "\nCurrent cash on hand : " << amount;
            if (gamesPlayed) {
                cout << "\nPercentage of winnings : " << float((gamesWon) / float(gamesPlayed * 100)) << "%";
            }
            else {
                cout << "\nPercentage of winnings : 0%";
            }
            cout << "\nTotal Games Played : " << gamesPlayed;
        }

        if (choice == 9) {

            cout << gamesWon;
            cout << "\n------Thank You.Visit Again!!-------";
            break;
        }
    }
    return 0;
}

