#include <iostream>
#include <stdlib.h> 
#include <iomanip>
using namespace std;

//Function declaration
void admin();
int Menu(int Response);
void Help();
bool shuffle(int betPosition);
void status(int& noOfPlays, int& winCount, int& looseCount, int& finanacialStatus, bool result);

int main()

{
	admin();
	return 0;
}

// creating one admin function that calls all other functions
void admin()
{
	int  x = 0, betPosition{}, userInput{}, noOfPlays = 0, winCount = 0, looseCount = 0, finanacialStatus = 0;
	bool result;

	int Response;
	Response = Menu(userInput);

	// using while loop to repeat menu
	while (Response != 9)
	{
		if (Response == 1)
			Help();

		else if (Response == 2)
		{
			cout << "Enter your bet position : ";
			cin >> betPosition;
		}
		else if (Response == 3)

		{
			result = shuffle(betPosition);
			status(noOfPlays, winCount, looseCount, finanacialStatus, result);

		}
		else if (Response == 4)
		{
			cout << "Total Number of Plays : " << noOfPlays << endl;
			cout << "Total Number of Wins : " << winCount << endl;
			cout << "Total Number of looses : " << looseCount << endl;
			cout << "Finacial status :" << finanacialStatus << "$" << endl;
		}

		else if (Response == 9)
			return;
		Response = Menu(userInput);

	}

}

// Displays menu and takes user input
int Menu(int userInput)
{
	cout << "1. Help" << endl;
	cout << "2. Specify your betting position for the \"Three Cards\"" << endl;
	cout << "3. Start Shuffling the \"Three Cards\"" << endl;
	cout << "4. Check Player's Performance (Financial and number of win/lose)" << endl << endl;

	cout << "9. Quit this program" << endl;
	cin >> userInput;

	return userInput;
}

// Provides instruction about all the options in menu
void Help()
{
	cout << "Choose option 2 to specify your bet " << endl;
	cout << "Choose option 3 to shuffle" << endl;
	cout << "Chosse option 4 to check your performance" << endl;
	cout << "Choose option 9 to quit" << endl;

	return;
}

// shuffles the cards and generates a random number
bool shuffle(int betPosition)
{
	int card1, card2, card3, total;
	srand(time(NULL));
	card1 = rand() % 10;
	card2 = rand() % 10;
	card3 = rand() % 10;
	total = card1 + card2 + card3;

	if (total <= 15 && betPosition == 1)
		return true;
	if (total >= 16 && betPosition == 2)
		return true;
	if (total % 2 && betPosition == 3)
		return true;
	else
		return false;
}

// shows status of the player and displays the result
void status(int& noOfPlays, int& winCount, int& looseCount, int& finanacialStatus, bool result)
{
	if (result)
	{
		winCount++;
		finanacialStatus++;
		cout << "You won!!" << endl;
	}
	else
	{
		looseCount++;
		finanacialStatus--;
		cout << "you loose!!" << endl;
	}
	noOfPlays++;

}





