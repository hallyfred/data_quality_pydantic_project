from config.db_loader import load_database
import pandas as pd
import pandera as pa
from contract.schema import CadastroSchema


def extract_data(query: str) -> pd.DataFrame:
    settings = load_database()

    connection_string = settings.url
    print(f"Conexão com o banco de dados estabelecida: {connection_string}")


    with settings.connect() as conn, conn.begin():
        df_cadastros = pd.read_sql_query(query, conn)

        df_cadastros = CadastroSchema.validate(df_cadastros)

    return df_cadastros

if __name__ == "__main__":
    query = "SELECT * FROM public.cadastros"  
    df_cadastros = extract_data(query)
    schema_cadastros = pa.infer_schema(df_cadastros)


    with open("schema_cadastros.py", "w", encoding="utf-8") as file:
        file.write(schema_cadastros.to_script())


    print(df_cadastros.head())



def transform_data():
    # Transform the extracted data
    pass

def load_data():
    # Load the transformed data into the target system
    pass