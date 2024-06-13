from app.orm.db import *
import sqlalchemy as sa

def get_user_currency(user_id, session):
    sql = sa.select(
        User, Currency, UserCurrency
    ).join(
        User, UserCurrency.c.user_id==User.c.user_id
    ).join(
        Currency, UserCurrency.c.currency_type==Currency.c.currency_id
    ).where(
        User.c.user_id==user_id
    )
    result = session.execute(sql)
    return result

def get_pricing_item(item_id, session):
    sql = sa.select(
        Pricing
    ).where(
        Pricing.c.item_id==item_id
    )
    result = session.execute(sql)
    return result

def insert_transaction(user_id, item_id, total_item, session):
    sql = sa.insert(Transaction).values(
        user_id=user_id,
        item_id=item_id,
        total_item=total_item
    )
    insert_transaction = session.execute(sql)
    session.commit()
    return insert_transaction

def get_transaction(user_id, item_id, session):
    sql = sa.select(
        Transaction
    ).where(
        sa.and_(
            Transaction.c.user_id==user_id,
            Transaction.c.item_id==item_id
        )
    )
    transaction = session.execute(sql)
    return transaction

def update_transaction(user_id, item_id, total_item, session):
    sql = sa.update(
        Transaction
    ).where(
        sa.and_(
            Transaction.c.user_id==user_id,
            Transaction.c.item_id==item_id
        )
    ).values(
        total_item=total_item
    )
    update_transaction_total_item = session.execute(sql)
    session.commit()
    return update_transaction_total_item