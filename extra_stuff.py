# import itertools

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

#
#
# class Account:
#     transaction_counter = itertools.count(100)
#
#     def __init__(self, account_number, first_name, last_name):
#         self._account_number = account_number
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def account_number(self):
#         return self._account_number
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, new_first_name):
#         # if len(str(new_first_name).strip()) == 0:
#         #     raise ValueError("First name is required.")
#         # else:
#         self._first_name = Account.validate_name(new_first_name, "First Name")
#
#     @property
#     def last_name(self):
#         return self._last_name
#
#     @last_name.setter
#     def last_name(self, new_last_name):
#         # if len(str(new_last_name).strip()) == 0:
#         #     raise ValueError("Last name is required.")
#         # else:
#         self._last_name = Account.validate_name(new_last_name, "Last Name")
#
#     @staticmethod
#     def validate_name(value, field_title):
#         if value is None and len(str(value).strip()) == 0:
#             raise ValueError(f"{field_title} is required.")
#         return str(value).strip()
