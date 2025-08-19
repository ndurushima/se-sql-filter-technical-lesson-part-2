import sqlite3
import pandas as pd

conn = sqlite3.connect('pets_database.db')
cursor = conn.cursor()
cats_data = pd.read_sql("SELECT * FROM cats;", conn)
print(cats_data)


cat_age = pd.read_sql("""
    SELECT * FROM cats
    WHERE age >= 5;
""", conn)

print(cat_age)


cat_age_between = pd.read_sql("""
    SELECT * FROM cats
    WHERE age BETWEEN 1 AND 3;
""", conn)

print(cat_age_between)


owners_null = pd.read_sql("""
    SELECT * FROM cats
    WHERE owner_id IS NULL;
""", conn)

print(owners_null)


starts_with_m = pd.read_sql("""
    SELECT * FROM cats
    WHERE name LIKE 'M%';
""", conn)

print(starts_with_m)


substr_with_m = pd.read_sql("""
    SELECT * FROM cats
    WHERE substr(name, 1, 1) = "M";
""", conn)

print(substr_with_m)


second_letter_a = pd.read_sql("""
    SELECT * FROM cats
    WHERE name LIKE '_a__';
""", conn)

print(second_letter_a)


substr_letter_a = pd.read_sql("""
    SELECT * FROM cats
    WHERE length(name) = 4 AND substr(name, 2, 1) = "a";
""", conn)

print(substr_letter_a)


owner_id_1 = pd.read_sql("""
SELECT COUNT(owner_id)
  FROM cats
 WHERE owner_id = 1;
""", conn)

print(owner_id_1)

conn.close()