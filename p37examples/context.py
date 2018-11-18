"""`ContextVars` were new features introduced in Python 3.7.

`ContextVars` are particularly useful when context switching between
coroutines.
"""
import asyncio
from contextvars import ContextVar

request_id_ctx: ContextVar[int] = ContextVar('request_id', default=42)


async def perform_task(request_id: int):
    """Peform some sort of task that context switches."""
    # Note the new f strings in python 3.7
    print(f"Performing {request_id} ...")
    request_id_ctx.set(request_id)  # set the task ID here.

    await asyncio.sleep(1)  # context switch

    # Same value after resuming.
    # statements can be executed inside f strings.
    print(f"... resuming {request_id_ctx.get()}.")


async def _do_task():
    # Context should be passed from caller
    print(f"Performing {request_id_ctx.get()} ...")
    await asyncio.sleep(1)
    print(f"... resuming {request_id_ctx.get()}.")


async def perform_task_depth(request_id: int):
    """Perform some sort of task that context switches.

    Calls `_do_task` to actually execute the task.
    """
    request_id_ctx.set(request_id)

    # Here we call a new function
    await _do_task()


async def main():
    """Run main method for the module."""
    print("Perform tasks in parallel to demonstrate context variables.")
    await asyncio.gather(*(perform_task(i) for i in range(20)))
    print("Done\n\n")

    print("Perform tasks in parallel to demonstrate passing context variables")
    await asyncio.gather(*(perform_task_depth(i) for i in range(20)))
    print("Done")


if __name__ == '__main__':
    asyncio.run(main())
