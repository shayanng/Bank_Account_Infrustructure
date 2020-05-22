import itertools


# class ransactionID:
#     def __init__(self, start_id):
#         self._start_id = start_id
#
#     def __next__(self):
#         pass


# def transaction_ids(start_id):
#     while True:
#         start_id += 1
#         yield start_id


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
