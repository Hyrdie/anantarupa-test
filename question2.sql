select user_data.username, user_currency.amount, currencies.currency_name, items.item_name, 
pricing_item.price, user_currency.amount / pricing_item.price as total_item_user_can_buy, pricing_item.max_owned,
case when user_currency.amount / pricing_item.price >= pricing_item.max_owned then 'EXCEEDED ITEM LIMIT'
else 'UNDER ITEM LIMIT'
end as user_item_limit
from pricing_item
inner join currencies on currencies.currency_id=pricing_item.currency_id
inner join user_currency on user_currency.currency_type=pricing_item.currency_id
inner join items on items.item_id=pricing_item.item_id
inner join user_data on user_data.user_id=user_currency.user_id
and user_currency.user_id=3;