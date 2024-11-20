from sqlalchemy import select, table,MetaData
from sqlalchemy.orm import Mapped

import app.database.models as md


async def set_user(tg_id):
    async with md.async_session() as session:
        user = await session.scalar(select(md.User).where(md.User.tg_id == tg_id))
        if not user:
            session.add(md.User(tg_id=tg_id))
            await session.commit()

async def get_days():
    async with md.async_session() as session:
        result = await session.scalars(select(md.Lesson.name).where(md.Lesson.state != True))
        return result.all()





async def get_time( nameday: str):
    # Динамическое создание таблицы
    async with md.async_session() as session:
      table_obj = table(nameday, md.metadata, autoload_with=md.engine)

    # Запрос для получения данных
      stmt = select(table_obj.c.time).where(table_obj.c.time != True)

    # Выполнение запроса
      result = await session.scalars(stmt)

      return result.all()  # Возвращаем все результаты

