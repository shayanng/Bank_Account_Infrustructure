import numbers
from datetime import timedelta, datetime


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Time zone cannot be empty.")

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError("Hour offset must be an integer.")

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError("Minute offset must be an integer.")

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("must be between -59 and 59 (inclusive).")

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)
        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("offset must be between -12:00 and 14:00.")

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f"TimeZone(name = '{self.name}', "
                f"offset_hours = {self._offset_hours}, "
                f"offset_minutes = {self._offset_minutes}")



    # @offset.

tz1 = TimeZone("ABC", -2, -15)
tz1.name

dt = datetime.utcnow()

print(dt)
print(dt + tz1.offset)
