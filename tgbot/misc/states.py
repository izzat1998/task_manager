from aiogram.dispatcher.filters.state import StatesGroup, State


class Tasks(StatesGroup):
    new_tasks = State()
    history = State()

