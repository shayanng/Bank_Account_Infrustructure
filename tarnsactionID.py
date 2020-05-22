import itertools


class Account:
    transaction_counter = itertools.count(100)

    def make_transaction(self):
        new_transaction_id = next(Account.transaction_counter)
        return new_transaction_id




acc1 = Account()
acc2 = Account()

print(acc1.make_transaction())
print(acc2.make_transaction())
print(acc1.make_transaction())
