from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, create_engine, Table, text


engine = create_engine('sqlite:///:memory:')

metadata_obj = MetaData()
user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(40), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False),
)

user_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_value", String(100)),
)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)
    
metadata_bd_obj = MetaData()

financial_info = Table(
    "financial_info",
    metadata_bd_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False),
)


for table in metadata_bd_obj.sorted_tables:
    print(table)

    
sql = text('select * from user')
with engine.connect() as conn:
    result = conn.execute(sql).fetchall()
for row in result:
    print(row)


    
# sql_insert = text("insert into user values(1,'juliana', 'email@email.com', 'ju')")
# with engine.connect() as conn:
#     result=conn.execute(sql_insert)