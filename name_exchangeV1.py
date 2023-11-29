
""" 
flatened_list (people)
buyers #copy of flatened_list
recipients #copy of flatened_list
gift_exchange #final complete list where each person in the fletened_list is a buyer as well as a recipient
for buyer in flatened_list #loop over each person
    randomly select a recipient for the buyer from the reciepients list
    ensure the the recipeint for the buyer is not thier parter from the orignal couples_list
    add the recipient to the buyer in the gift_exchange dictionary
    remove the buyer from the buyers list
    remove the recipient from the reciepts list
 """
import random

def generate_gift_exchange(couples):
    # Create a reversed dictionary
    reversed_couples = {v: k for k, v in couples.items() if v is not None}
    flattened_list = list(set([person for couple in couples.items() for person in couple if person is not None]))
    buyers = flattened_list.copy()
    recipients = flattened_list.copy()
    gift_exchange = {person: None for person in flattened_list}

    for buyer in flattened_list:
        # Randomly select a recipient for the buyer from the recipients list
        recipient = random.choice(recipients)

        # Ensure that the recipient for the buyer is not their partner from the original couples or the reversed_couples
        partner = couples.get(buyer, None)
        reversed_partner = reversed_couples.get(buyer, None)
        while recipient == partner or recipient == reversed_partner:
            recipient = random.choice(recipients)

        # Ensure that a buyer is not buying for themselves
        while recipient == buyer:
            recipient = random.choice(recipients)

        # Add the recipient to the buyer in the gift_exchange dictionary
        gift_exchange[buyer] = recipient

        # Remove the buyer from the buyers list and the recipient from the recipients list
        buyers.remove(buyer)
        recipients.remove(recipient)

    return gift_exchange

# Example usage:
couples_list = {'Drew': 'Brandy', 'Cassie': 'Tony', 'Chad': 'Lundy', 'Courtney': 'Rex', 'Zach': 'JayLynn', 'Tyler': None}
gift_exchange_result = generate_gift_exchange(couples_list)

for buyer, recipient in gift_exchange_result.items():
    print(f"{buyer} is buying for {recipient}")
