
import typing


class Record:
	def __init__(self, time: str, values: dict):
		self.time = time
		self.values = values

	def get(self, name: str) -> typing.Any:
		return self.values.get(name)


class Result:
	def __init__(self, records: list[Record]):
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
		raise StopIteration


