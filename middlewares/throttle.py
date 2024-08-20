import asyncio
import time
from typing import Any, Awaitable, Callable, Dict

from aiogram.types import Update
from aiogram.dispatcher.middlewares.base import BaseMiddleware

class ThrottleMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: float = 0.5) -> None:
        self.rate_limit = rate_limit
        self.user_last_message_time = {}
        super().__init__()
    
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user_id = (event.message.from_user or event.callback_query.from_user).id
        chat_id = (event.message.chat or event.callback_query.message.chat).id
        current_time = time.time()
        
        last_message_time = self.user_last_message_time.get(user_id, 0)

        if (current_time - last_message_time) < self.rate_limit:            
            await event.bot.send_message(
                chat_id=chat_id,
                text="Too many attempts. Please try again later."
            )
            return  
        
        self.user_last_message_time[user_id] = current_time

        return await handler(event, data)
