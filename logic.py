from database import DatabaseConfig

async def registration(db:DatabaseConfig, user, password_hash):
   
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
            INSERT INTO users (username, password)
            VALUES ($1, $2)
    """, user, password_hash)
    except Exception as e:
        print('Error',e)


async def login(db:DatabaseConfig,username, password):
    
    try:
        async with db.pool.acquire() as conn:
            user = await conn.fetchrow("""
        SELECT id FROM users WHERE username = $1 and password = $2
    """,username, password)
            return user if user else None
        
    except Exception as e:
        print('Error',e)


async def create_task(db:DatabaseConfig, title:str, description:str, user_id:str):
    
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO todos(title, description, user_id)
                VALUES($1, $2, $3)
        """, title, description, user_id)
    except Exception as e:
        print('Error:',e)


async def get_tasks(db:DatabaseConfig, user_id):
    
    try:
        async with db.pool.acquire() as conn:
            tasks = await conn.fetch("""
        SELECT * FROM todos WHERE user_id = $1; 
        """,user_id)
            return tasks
        
    except Exception as e:
        print('Error', e)


async def update_task(db:DatabaseConfig, task_id:int, title:str, description: str):
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
    UPDATE todos SET title=$1, description=$2 WHERE id=$3
""",title, description, int(task_id))
            print('Task updated!')
    
    except Exception as e:
        print('Error:', e)


async def delete_task(db:DatabaseConfig, task_id:int):
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
    DELETE FROM todos WHERE id=$1
""", int(task_id))
        print('Task deleted!')

    except Exception as e:
        print('Error:',e)  



async def get_task_by_id(db:DatabaseConfig, task_id:int):
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
    SELECT * FROM todos WHERE id=$1
""", int(task_id))
            
    except Exception as e:
        print('Error',e)

# async def delete_user(db:DatabaseConfig, user_id):
    
#     try:
#         async with db.pool.acquire() as conn:
#             result = await conn.execute("""
#                     DELETE FROM users 
#                     WHERE id = $1
#         """,user_id)
#         return result
#     except Exception as e:
#         print('Error',e)

