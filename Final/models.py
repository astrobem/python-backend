import typing


class Record:
    __keys = ["force", "temperature", "pressure", "altitude_bmp", "acceleration_x", "acceleration_y", "acceleration_z",
              "time",
              "rotation_x", "rotation_y", "rotation_z", "lat", "lng", "altitude", "rssi"]

    def __init__(self, *values):
        if len(self.__keys) != len(values):
            raise AttributeError(f"Invalid number of values, {len(values)} passed, {len(self.__keys)} expected")

        self.__values = values

        values = iter(list(values))
        for name in self.__keys:
            setattr(self, f"{name}", next(values))
        return

    @property
    def values(self) -> dict:
        return dict(zip(self.__keys, self.__values))

    def get(self, name: str) -> typing.Any:
        return self.values.get(name)


class Result:
    def __init__(self, records: typing.List[Record]):
        self.__records: list = records
        self.__current = 0

    def __len__(self):
        return len(self.__records)

    def __iter__(self):
        return self

    def __next__(self):
        self.__current += 1
        if self.__current < len(self.__records):
            return self.__records[self.__current]
        self.__current = 0
        raise StopIteration
