import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_scoped_session
from sqlalchemy.orm import sessionmaker

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_factory = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)


AsyncScopedSession = async_scoped_session(
    async_session_factory,
    scopefunc=asyncio.current_task
)


async def get_async_session() -> AsyncSession:
    async with AsyncScopedSession() as session:
        yield session


if __name__ == "__main__":
    print(DATABASE_URL)