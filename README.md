# Brief Overview
Junior year project for AP Statistics. Probability wheel that automatically detects the slot which the user lands on, and uploads their cumulative score to a database of other users. The frame was designed in solidworks and 3d printed, the program was developed in Python and runs on a Raspberry Pi. The database is programmed in SQL.

# Game Objective
The objective of the game is to outscore your opponent in this two player turn-based game of luck.

You will acumulate points by spinning the wheel and gaining the amount of points you land on, ranging from 100 to 1000. However, there are two bad spaces on the wheel. Landing on the "-100" space will cause you to lose 100 points. Landing on the "𝝅" space will cause you to instantly lose the game.

There is no strategy, the game is completely based on chance. Are you feeling lucky? Try and earn the highset score.

# How to Play
The players will take turns spinning the wheel a total of three times each. Whoever is youngest between the two players will spin first.

The wheel must make at least one full rotation to be counted as a valid spin. The game ends after each player has spun the wheel three times or if a player lands on the "𝝅" space.

The loser of the game must face a consequence and the winner can brag about their luck.

# Design and Building
We devised the game with the object of completing two main automated tasks: data collection and data analysis. To collect the data, we make use of nfc(near field communication) tags placed at the back of each segment of the wheel. This technology is similar to the “tap to pay” technology used within your iPhones or credit cards except as opposed to reading your credit card information, we are reading the distinct id of that specific nfc tag. Within our program, each tag is then paired with a corresponding point value. To read each nfc tag, there is a rfid chip(pn532) that is placed at the back of the wheel. The catch with nfc, however, is that the signal needs to be within 3cm of the chip. With typical spin the wheel games, that would be impossible because the wheel can land at any portion of each segment. To combat this issue, we 3d modeled two disks that have magnets with opposing polarity. This makes sure that on every roll, the wheel lands exactly in the center and the nfc tag is within the 3cm limit of the nfc chip. When the nfc chip detects the nfc tag, the information is sent down and processed by a raspberry pi. This handled the automatic data collection process. To store this data to be analyzed, we utilize a MariaDB MySQL database. This data is queried into the database at the end of each user’s turn. With the data stored automatically, that allows us to perform analysis on every turn that every player takes. We compute and display the percentile that every player is in subsequent to every turn they take. Finally, once the player is done, they can view their performance on the leaderboard, which lists the best performances in order of their point total.
