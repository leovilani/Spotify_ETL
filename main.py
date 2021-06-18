import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "Leonardo"
TOKEN = "BQBn1QTCFGRGaJH9RM2e3OrT79lnf3fhQV0HrKy9NfReY_XudMKleE_xDj2C31xXNsynkgB1EF9cG7CaB0JUuYxn6mO9yeTFbvuBI7Q5m2pyZGlXllYl5BWR68MwoXRrkddizmXb6sQcsIcmtZazSfK9uU5T6R9zV9S4"

# Gere seu token aqui: https://developer.spotify.com/console/get-recently-played/
# Nota: você precisa de uma conta no Spotify.


def check_valid_data(df: pd.DataFrame) -> bool:
    # Checa se o dataframe está vazio
    if df.empty:
        print("Nenhuma música encontrada. Finalizando execução.")
        return False

    # Checa Primary Key
    if pd.Series(df["played_at"]).is_unique:
        pass
    else:
        raise Exception("Chave Primária repetida")

    # Checa por nulls
    if df.isnull().values.any():
        raise Exception("Valor Null encontrado ")

    return True


if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    # Converte tempo em milisegundos
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Baixa dados das musicas que você escutou nas ultímas 24 horas
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}"
                     .format(time=yesterday_unix_timestamp), headers=headers)

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    # Extrai apenas os dados relevantes do objeto json.
    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    # Prepara o dicionário para se tornar um dataframe do pandas
    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns=["song_name", "artist_name", "played_at", "timestamp"])

    # Validação
    if check_valid_data(song_df):
        print("Dados validos")

    # Carregar dados para banco de dados
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS my_played_tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        timestamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    cursor.execute(sql_query)
    print("Banco de dados aberto com sucesso")

    try:
        song_df.to_sql("my_played_tracks", engine, index=False, if_exists='append')
    except:
        print("Dados já existem no banco de dados")

    conn.close()
    print("Banco de dados fechado")
