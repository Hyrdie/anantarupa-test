from sqlalchemy.orm import Session
from app.orm.db_setup import engine
from app.repository.purchase import *

def purchase(user_id, item_id, qty):
    with Session(engine) as session:
        user_currency = get_user_currency(user_id, session)
        item_price = get_pricing_item(item_id, session).fetchone()

        if item_price is None:
            return "Error: Item not found"

        total_amount_currency = 0
        for currency in user_currency:
            if item_price.currency_id == currency.currency_type:
                if currency.amount < item_price.price*qty:
                    return "Error: doesnt have enough currency to buy this item"
                if qty >= item_price.max_owned:
                    return "Error: exceeded item limit"
                
                total_amount_currency = item_price.price*qty
        
        transaction_data = get_transaction(user_id, item_id, session).fetchone()

        if transaction_data is None:
            insert_transaction(
                user_id=user_id,
                item_id=item_price.id,
                total_item=qty,
                session=session
            )
        
        
        
        total_item_user = transaction_data.total_item+qty
        if total_item_user > item_price.max_owned:
            return f"Error: exceeded item limit. user already have {transaction_data.total_item} item(s) before this transaction"
        
        update_currency_user(
            user_id=user_id,
            currency_id=item_price.currency_id,
            amount=total_amount_currency,
            session=session
        )

        update_transaction(
            user_id=user_id,
            item_id=item_id,
            total_item=total_item_user,
            session=session
        )

    return "Success"