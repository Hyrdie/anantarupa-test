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
    