from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.purchase import *

def purchase(user_id, item_id, qty):
    with Session(engine) as session:
        user_currency = get_user_currency(user_id, session)
        item_price = get_pricing_item(item_id, session)
    
    if item_price.first() is None:
        return "Error: Item not found"

    for item in item_price:
        for currency in user_currency:
            if item.currency_id == currency.currency_type:
                print("user currency : ", currency.currency_name)
                print("user currency : ", currency.amount)
                print("total harga : ", item.price*qty)
                if currency.amount < item.price*qty:
                    return "doesnt have enough currency to buy this item"
                if qty >= item.max_owned:
                    return "exceeded item limit"
    
    return "Success"