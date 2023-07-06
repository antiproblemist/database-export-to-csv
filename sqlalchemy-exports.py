import pandas as pd, os
from tqdm import tqdm
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

base_folder_input = input("Enter the base folder/project name: ") # Here you enter the Project Name when prompted

db_engine = "postgresql" # Database engine (Tested with PostgreSQL)
db_username = "<DATABASE_USERNAME>" # Your Database Username
db_password = "<DATABASE_PASSWORD>" # Your Database Password
db_host = "<DATABASE_HOST>" # Your Database Host eg. mydbhost.ap-south-1.rds.amazonaws.com
db_port = "<DATABASE_PORT>" # Your Database Port eg. 5432
db_name = "<DATABASE_NAME>" # Your Database Name

batch_size = 10000 # This will be used in Limit and Offset for the Database queries

base_folder_name = "%s %s" % (base_folder_input, f"{datetime.now():%d-%b-%y %H %M %S}")

engine = create_engine("%s://%s:%s@%s:%s/%s" % 
	(db_engine, db_username,db_password, db_host, db_port, db_name),
	pool_size=20,
	max_overflow=0)

metadata = MetaData(engine)

Base = automap_base(metadata=metadata)
Base.prepare(reflect=True)

tables = Base.classes.keys()

if not os.path.exists(base_folder_name):
    os.mkdir(base_folder_name)

for table in tables:
	table_model = Base.classes.get(table)
	df = pd.DataFrame()
	session = Session(engine)
	count = session.query(table_model).count()
	offset = 0

	print("\r\n\r\nProcessing %s" % table)
	pbar = tqdm(total=count)

	while offset <= count:
		records = session.query(table_model).limit(batch_size).offset(offset)
		list_of_records = []

		for curr in records:
			data = {}
			for column in table_model.__mapper__.columns:
				data[column.name] = getattr(curr, column.name)
			list_of_records.append(data)

		temp_df = pd.DataFrame.from_dict(list_of_records)
		df = pd.concat([df, temp_df])

		offset = offset + batch_size
		pbar.update(batch_size)

	filename = os.path.join(base_folder_name, "%s.csv" % table)
	df.to_csv(filename, index=False, encoding='utf-8')