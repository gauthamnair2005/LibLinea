# Data Analysis and Data Science utilities for Linea

import pandas as pd
from liblinea import Linea

class Basic:
    @staticmethod
    def toCSV(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_csv(filename, index=False)

    @staticmethod
    def toExcel(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_excel(filename, index=False)

    @staticmethod
    def toJSON(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_json(filename, orient='records', lines=True)

    @staticmethod
    def toHTML(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_html(filename, index=False)

    @staticmethod
    def toMarkdown(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            with open(filename, 'w') as f:
                f.write(df.to_markdown(index=False))

    @staticmethod
    def toParquet(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_parquet(filename, index=False)

    @staticmethod
    def toPickle(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_pickle(filename)

    @staticmethod
    def toSQL(data, table_name, conn):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_sql(table_name, conn, if_exists='replace', index=False)

    @staticmethod
    def toClipboard(data):
        df = Linea.createDataFrame(data)
        if df is not None:
            df.to_clipboard(index=False)

    @staticmethod
    def toLaTeX(data, filename):
        df = Linea.createDataFrame(data)
        if df is not None:
            with open(filename, 'w') as f:
                f.write(df.to_latex(index=False))