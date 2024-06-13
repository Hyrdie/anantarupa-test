from app.orm.db_setup import metadata
from sqlalchemy import (Table, Column, Integer, Text, JSON, String, Enum, ForeignKey, Time, DateTime)

User = Table(
    'user_data',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('username', String),
    Column('join_date', Time)
)

Currency = Table(
    'currencies',
    metadata,
    Column('currency_id', Integer, primary_key=True),
    Column('currency_name', String),
)

Item = Table(
    'items',
    metadata,
    Column('item_id', Integer, primary_key=True),
    Column('item_name', String),
)

UserCurrency = Table(
    'user_currency',
    metadata,
    Column('user_currency_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user_data.user_id")),
    Column('currency_type', Integer, ForeignKey("currencies.currency_id")),
    Column('amount', Integer),
)

Pricing = Table(
    'pricing_item',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('item_id', Integer, ForeignKey("items.item_id")),
    Column('price', Integer),
    Column('currency_id', Integer, ForeignKey("currencies.currency_id")),
    Column('max_owned', Integer)
)

Transaction = Table(
    'transaction',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user_data.user_id")),
    Column('item_id', Integer, ForeignKey("items.item_id")),
    Column('total_item', Integer),
)