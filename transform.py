import pandas as pd
import re
from sqlalchemy import create_engine
#import datetime
#from dbfpy3 import dbf

class transformer:
    def __init__(self) -> None:
        pass

    def from_csv(self, filename: str) -> pd.DataFrame:
        df = pd.read_csv(filename)
        return df
    
    def fit_transform(self, df : pd.DataFrame) -> pd.DataFrame:
        data = pd.DataFrame(
            data= {
                "OID" : range(len(df)),
                "Id": range(len(df)),
                "POINT_X" : df.Longitud.apply(lambda x: re.sub(r'[\'\[\]]', '', x)),
                "POINT_Y" : df.Latitud.apply(lambda x: re.sub(r'[\'\[\]]', '', x))
            }
        ).set_index("OID")
        data2 = pd.concat(
            [data, df.drop(['Latitud', 'Longitud', 'Azimuth','IMEI'], axis=1)], axis=1)
        return data, data2
    
    # Nueva propuesta, a postgres para MXGIS
    # Requisitos de librerías: sqlalchemy y psycopg2
    def to_postgres(self, d1: pd.DataFrame, d2: pd.DataFrame, 
                    table_name: str, username: str, password: str, 
                    host: str, database: str):
        # establecer conexión a la base de datos con SQLAlchemy
        engine = create_engine(f'postgresql://{username}:{password}@{host}/{database}')
        
        # escribir dataframe 1 en la tabla correspondiente de la base de datos
        d1.to_sql(table_name, engine, if_exists='replace', index=False)
        
        # escribir dataframe 2 en la tabla correspondiente de la base de datos
        d2.to_sql(table_name, engine, if_exists='append', index=False)
        
        # cerrar conexión a la base de datos
        engine.dispose()
    """
    Salida a archivo tipo dbf, para su posterior uso, no funciona debido a la librería pydbf#
    def to_dbf(self, d1: pd.DataFrame, d2: pd.DataFrame) -> None:
        def write_df_to_dbf(df, filename):
            # Crear un nuevo archivo dbf
            dbfn = dbf.Dbf(filename, new=True)
            
            # Agregar los campos del archivo dbf
            for columna in df.columns:
                dbfn.add_field(columna, df[columna].dtype, size=80)
            
            # Escribir los datos del DataFrame
            for i, fila in df.iterrows():
                rec = dbfn.new_record()
                for j, columna in enumerate(df.columns):
                    if df[columna].dtype == 'datetime64[ns]':
                        fecha = datetime.datetime.strftime(fila[columna], '%Y%m%d')
                        rec[j] = fecha
                    else:
                        rec[j] = fila[columna]
                dbfn.write_record(rec)
            
            dbfn.close()
        
        # Escribir d1 en su propio archivo dbf
        write_df_to_dbf(d1, "archivo1.dbf")
        
        # Escribir d2 en su propio archivo dbf
        write_df_to_dbf(d2, "archivo2.dbf")
    """
