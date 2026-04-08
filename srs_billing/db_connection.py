from sqlalchemy import create_engine, text

try:
    database = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/srs_billing")

    with database.connect() as conn:
        result = conn.execute(text("SELECT id, email FROM \"users\""))
        for row in result:
            print(row)

except Exception as e:
    print(f"❌ Database Connection Error: {str(e)}")
    import traceback


    traceback.print_exc()