import sqlite3
import pandas as pd

 # Calculating the mean values of the columns in the human_resources table so we can fill in nulls

def get_data():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country,
           CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) AS Psychologists,
           CAST([Nurses working in mental health sector (per 100 000 population)] AS float) AS Nurses,
           CAST([Social workers working in mental health sector (per 100 000 population)] AS float) AS Social_Workers,
           CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float) AS Psychiatrists,
           CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
           + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
           + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
           + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
           FROM human_resources;"""

    df_with_nulls = pd.read_sql_query(q, con=conn)

    return df_with_nulls


# Creating DataFrames with populations of interest

def get_btsx_above():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                        FROM human_resources 
                        WHERE total_mh_personnel >= 30.601)
            LEFT JOIN suicide_rate
            USING(Country)
            WHERE Sex = "Both sexes";"""

    df_suicide_rate_btsx_above = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_btsx_above


def get_btsx_below():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                 FROM human_resources 
                 WHERE total_mh_personnel < 30.601)
            LEFT JOIN suicide_rate
            USING(Country)
            WHERE Sex = "Both sexes";"""

    df_suicide_rate_btsx_below = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_btsx_below


def get_male_above():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                 FROM human_resources 
                 WHERE total_mh_personnel >= 30.601)
           LEFT JOIN suicide_rate
           USING(Country)
           WHERE Sex = "Male";"""

    df_suicide_rate_male_above = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_male_above


def get_male_below():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                 FROM human_resources 
                 WHERE total_mh_personnel < 30.601)
           LEFT JOIN suicide_rate
           USING(Country)
           WHERE Sex = "Male";"""

    df_suicide_rate_male_below = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_male_below 



def get_female_above():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                 FROM human_resources 
                 WHERE total_mh_personnel >= 30.601)
           LEFT JOIN suicide_rate
           USING(Country)
           WHERE Sex = "Female";"""

    df_suicide_rate_female_above = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_female_above


def get_female_below():

    conn = conn=sqlite3.connect("/Users/flatironschool/Desktop/who_suicide.db")
    c=conn.cursor()

    q = """SELECT Country, 
                  CAST([15-29  years] AS float) AS [15-29  years]
           FROM (SELECT Country,
                        COALESCE([Psychologists working in mental health sector (per 100 000 population)], 9.705),
                        COALESCE([Nurses working in mental health sector (per 100 000 population)], 12.664),
                        COALESCE([Social workers working in mental health sector (per 100 000 population)], 3.364),
                        COALESCE([Psychiatrists working in mental health sector (per 100 000 population)], 4.868),
                        CAST([Psychiatrists working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Nurses working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Social workers working in mental health sector (per 100 000 population)] AS float)
                        + CAST([Psychologists working in mental health sector (per 100 000 population)] AS float) as total_mh_personnel
                 FROM human_resources 
                 WHERE total_mh_personnel < 30.601)
           LEFT JOIN suicide_rate
           USING(Country)
           WHERE Sex = "Female";"""

    df_suicide_rate_female_below = pd.read_sql_query(q, con=conn)

    return df_suicide_rate_female_below



