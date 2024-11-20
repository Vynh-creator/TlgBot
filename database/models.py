from sqlalchemy import BigInteger, String, ForeignKey,MetaData,TIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url="sqlite+aiosqlite:///db.sqlite3")
async_session = async_sessionmaker(engine)
metadata=MetaData()

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    is_banned: Mapped[bool] = mapped_column()
    rec: Mapped[bool] = mapped_column()


class Lesson(Base):
    __tablename__ = "days"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    state: Mapped[bool]= mapped_column()


class Monday(Base):
    __tablename__ = "monday"
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[str] = mapped_column(String(20))
    time: Mapped[str] = mapped_column()
    person1: Mapped[bool] = mapped_column()
    person2: Mapped[bool] = mapped_column()
    person3: Mapped[bool] = mapped_column()
    person4: Mapped[bool] = mapped_column()
    person5: Mapped[bool] = mapped_column()


class Tuesday(Base):
    __tablename__ = "tuesday"
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[str] = mapped_column(String(20))
    time: Mapped[str] = mapped_column()
    person1: Mapped[bool] = mapped_column()
    person2: Mapped[bool] = mapped_column()
    person3: Mapped[bool] = mapped_column()
    person4: Mapped[bool] = mapped_column()
    person5: Mapped[bool] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
