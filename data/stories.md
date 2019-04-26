## goodbye
 * goodbye
 - utter_goodbye

## thank
 * thank
 - utter_thank

## greet
 * greet
	- utter_greet

## ask
 * ask
	- utter_ask

## ask
* greet
	- utter_greet
* ask
	- utter_ask
* thank
	- utter_thank


## ask
* greet
	- utter_greet
* ask
	- utter_ask
* thank
	- utter_thank
* goodbye
	- utter_goodbye


## affirm
* affirm
 - utter_affirm


## resturant_search1
 * greet
	- utter_greet
 * restaurant_search
	- action_askrestaurant
	- slot{"requested_slot": "cuisine"}
 * inform{"cuisine": "mexican"}
	- action_askrestaurant
	- slot{"cuisine": "mexican"}
	- slot{"requested_slot": "location"}
* restaurant_search{"location": "bangalore"}
	- slot{"location": "bangalore"}
	- utter_ask


