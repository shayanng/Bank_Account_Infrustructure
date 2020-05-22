import itertools
from timezone import TimeZone


class Account:
    transaction_counter = itertools.count(100)

    def __init__(self, account_number, first_name, last_name, time_zone=None, initial_balance=0):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        if time_zone is None:
            time_zone = TimeZone("UTC", 0, 0)
        self.time_zone = time_zone

        self._balance = float(initial_balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        # if len(str(new_first_name).strip()) == 0:
        #     raise ValueError("First name is required.")
        # else:
        # self._first_name = Account.validate_name(new_first_name, "First Name")
        self.validate_and_set_name("_first_name", new_first_name, "First Name")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        # if len(str(new_last_name).strip()) == 0:
        #     raise ValueError("Last name is required.")
        # else:
        self.validate_and_set_name("_last_name", new_last_name, "Last Name")

    @property
    def balance(self):
        return self._balance

    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError("must be a valid TimeZone object.")
        self._time_zone = value

    # @staticmethod
    def validate_and_set_name(self, attribute_name, value, field_title):
        if value is None and len(str(value).strip()) == 0:
            raise ValueError(f"{field_title} is required.")
        setattr(self, attribute_name, value)


    def make_transaction(self):
        new_transaction_id = next(Account.transaction_counter)
        return new_transaction_id




# acc1 = Account()
# acc2 = Account()
#
# print(acc1.make_transaction())
# print(acc2.make_transaction())
# print(acc1.make_transaction())


a = Account(65245, "Shayan", "Naghi", initial_balance=1_000_000)
print(a.first_name)
print(a.last_name)
a.last_name = "Naghizadeh"
print(a.first_name)
print(a.last_name)

print(a.balance)

