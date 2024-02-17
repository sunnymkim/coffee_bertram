README

    HOW TO ENTER INPUT:

    NOTE: General info about people/prices is saved into separate file so user does not need to input info every time they use the program

    In input.txt, enter the corresponding information in the format specified:
    First line should be the number of employeed involved. 
    Second line should be the names of the employees separated by a space
    Third line should be the prices of each employee's drink

    HOW TO RUN PROGRAM:

    Once input.txt is set up, run coffee.py by typing "python python.py" in your local terminal. 
    Type in the current day (number of days since you started using the program) as prompted. 
    The program will output today's payer. When asked for extra info, answer yes or no accordingly.

    IMPORTANT NOTE:
    It is difficult to allow every person to pay exaclty the amount of money they should be paying for without making the total number of days in one paying cycle a very big number. This is because we ideally want to match the ratio of price per person to total price to the ratio of days each per person pays to total number of days in one cycle. However, the second ratio requires whole number in the numerator and denominator, so scaling the prices to whole number would make the total number of days a very big number. 

    Thus, to simplify the program slightly, we round each price to the nearest $.5. In doing so, the total number of days will not become too long. To be tramsparent about this modification, we calculate the total number of money a person overpays/underpays per day. This value can be seen be answering "Y" to the "EXTRA INFO?" prompt. 

    OHTER FILES:
    I process.ipynb to test out my code in smaller parts. # coffee_bertram
