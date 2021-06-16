from models.manufacturer import Manufacturer
from models.stock import Stock

import repositories.manufacturer_repository as manufacturer_repository
import repositories.stock_repository as stock_repository

manufacturer_repository.delete_all()
stock_repository.delete_all()

manufacturer1 = Manufacturer("Onyxhand","Dustcounter")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("Galan","Thetris")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Kormdek","Bronzebrowser")
manufacturer_repository.save(manufacturer3)
#  name, description , manufacturer ,cost, price 
stock_1 = Stock("Bag of holding", "Wondrous Item",  manufacturer1, 100 , 175)
stock_repository.save(stock_1)
stock_2 = Stock("Ivory Goat", "Wonderous Item", manufacturer1, 300, 424)
stock_repository.save(stock_2)

stock_3 = Stock("Necklace Of Fireballs", "Wonderous Item", manufacturer2, 400, 510)
stock_repository.save(stock_3)
stock_4 = Stock("Ring Of Feather Falling", "Wonderous Item", manufacturer2, 2000, 3250)
stock_repository.save(stock_4)

stock_5 = Stock("Flame Tongue", "Weapon(greatsword)",manufacturer3, 4000,5550)
stock_repository.save(stock_5)
stock_6 = Stock("Vorpal Sword", "Weapon(legendary)",manufacturer3, 20000,45000)
stock_repository.save(stock_6)

# stock_7 = Stock("cast-off Armor", "armor(common)",manufacturer1, 400,650)
# stock_repository.save(stock_7)
# stock_8 = Stock("Hat of Wizardry", "Wondrous item(common)",manufacturer2, 500,700)
# stock_repository.save(stock_8)
# stock_9 = Stock("Pipe of Smoke Monsters", "Wondrous item(common)",manufacturer3, 54,65)
# stock_repository.save(stock_9)
# stock_10 = Stock("Clockwork Amulet", "wondrous item(common)",manufacturer1, 400,500)
# stock_repository.save(stock_10)

manufacturer_repository.select_all()