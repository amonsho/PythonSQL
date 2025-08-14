import asyncpg

class DatabaseConfig:
    def __init__(self, user, password, db_name, port=5432, host='localhost'):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = port
        self.host = host
        self.pool = None

    async def connect(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=self.user,
                password=self.password,
                database=self.db_name,
                port=self.port,
                host=self.host
            )
        except Exception as e:
            print('Error',e)
    
    async def close(self):
        await self.pool.close()

    async def create_table(self):
        try:
            async with self.pool.acquire() as conn:
                await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS todos (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                created_at DATE DEFAULT CURRENT_DATE,
                user_id INT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
    """)
        except Exception as e:
            print('Error',e)


# async def get_db() -> DatabaseConfig:
#     try:
#         db=DatabaseConfig(
#             user='postgres',
#             password='Am.on$sh_op',
#             db_name='todo'
#         )
#         await db.connect()
#         await db.create_table()
#         return db
#     except Exception as e:
#         print('Error',e)