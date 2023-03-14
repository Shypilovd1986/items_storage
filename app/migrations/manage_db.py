"""module with functions for working with database"""
import mysql.connector as conn


def connect_to_our_database(db_name):
    """function for connection to database"""
    try:
        db_connect = conn.connect(
            host="localhost",
            user="root",
            password="19865421",
            database=db_name
        )
        return db_connect
    except Exception as error:
        print(error)


def add_new_brand(brand_name: str, brand_colour: str):
    """function for adding new brand to Brands table """
    project_db = connect_to_our_database('items_storage')
    try:
        cursor = project_db.cursor()
        cursor.execute(f"INSERT INTO brands(brand_name, country_of_origin) "
                       f"VALUES (\"{brand_name}\",\"{brand_colour}\"); ")
        project_db.commit()
        project_db.close()
        return True
    except Exception as err:
        print(err)


# if __name__ == '__main__':
#     db = connect_to_our_database('items_storage')
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM items")
#     items_records = cursor.fetchall()
#     print(items_records)
#     db.close()
