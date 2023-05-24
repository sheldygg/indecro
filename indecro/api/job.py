import asyncio
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Protocol

from indecro.api.executor import Executor
from indecro.api.rules import Rule
from indecro.api.scheduler import Scheduler
from indecro.api.task import Task


@dataclass
class Job(Protocol):
    task: Task
    rule: Rule

    next_run_time: datetime

    daemonize: bool = False
    is_thread_safe: bool = False

    name: Optional[str] = None

    is_running: bool = False

    scheduler: Optional[Scheduler] = None
    executor: Optional[Executor] = None

    running_task: Optional[asyncio.Task] = None

    @abstractmethod
    async def schedule(self, reschedule: bool = True) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def execute(self, reschedule: bool = True) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()
