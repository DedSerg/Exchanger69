import time
import asyncio


async def start_strongman(name, power):
    print(f'Богатырь {name} начал поединок.')
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(f'Богатырь {name} опустошил {i} кубок.')
    print(f'Богатырь {name} закончил поединок.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Алёша', 3))
    task2 = asyncio.create_task(start_strongman('Добрыня', 4))
    task3 = asyncio.create_task(start_strongman('Илья', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
