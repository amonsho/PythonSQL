from database import get_db

async def create_user(user, password_hash):
    db = await get_db()
    try:
        async with db.pool.acquire() as conn:
            await conn.execute("""
            INSERT INTO users (username, password)
            VALUES ($1, $2)
    """, user, password_hash)
    except Exception as e:
        print('Error',e)


async def get_users():
    db = await get_db()
    try:
        async with db.pool.acquire() as conn:
            users = await conn.fetch("""
        SELECT * FROM users;
    """)
            return users
    except Exception as e:
        print('Error',e)

async def update_user(user_id:int, new_username, new_password):
    db = await get_db()
    try:
        async with db.pool.acquire() as conn:
            if new_username and new_password:
                await conn.execute("""
                    UPDATE users
                    SET username = $1, password = $2
                    WHERE id = $3
                """, new_username, new_password, user_id)
            elif new_username:
                await conn.execute("""
                    UPDATE users 
                    SET username = $1
                    WHERE id = $2
                """,new_username,user_id)
            elif new_password:
                await conn.execute("""
                    UPDATE users
                    SET password = $1
                    WHERE id = $2
                """, new_password, user_id)
            else:
                print('nothing update')
    except Exception as e:
        print('Error', e)


async def get_user_by_id(user_id):
    db = await get_db()
    try:
        async with db.pool.acquire() as conn:
            user = await conn.fetch("""
                SELECT * FROM users
                WHERE id = $1
        """,user_id)
            return user
    except Exception as e:
        print('Error', e)

async def delete_user(user_id):
    db = await get_db()
    try:
        async with db.pool.acquire() as conn:
            result = await conn.execute("""
                    DELETE FROM users 
                    WHERE id = $1
        """,user_id)
        return result
    except Exception as e:
        print('Error',e)