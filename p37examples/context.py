"""`ContextVars` were new features introduced in Python 3.7.

`ContextVars` are particularly useful when context switching between
coroutines.
"""
import asyncio
from contextvars import ContextVar

request_id_ctx: ContextVar[int] = ContextVar('request_id', default=42)


async def perform_task(request_id: int):
    """Peform some sort of task that context switches.
    """
    # Note the new f strings in python 3.7
    print(f"Performing {request_id} ...")
    request_id_ctx.set(request_id)  # set the task ID here.

    await asyncio.sleep(5)  # context switch

    # Same value after resuming.
    # statements can be executed inside f strings.
    print(f"... resuming {request_id_ctx.get()}.")


async def main():
    # Perform tasks in parallel
    await asyncio.gather(*(perform_task(i) for i in range(20)))


if __name__ == '__main__':
    asyncio.run(main())
