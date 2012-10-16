#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
book_price = 24.95
store_discount = 0.4
first_copy_shipping_price = 3
additional_shipping_price = 0.75

first_copy_price = (book_price * store_discount) + first_copy_shipping_price
_59_copies_price = 59 * ((book_price * store_discount) + additional_shipping_price)
_60_copies_price = first_copy_price + _59_copies_price

print (_60_copies_price)
