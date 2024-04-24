# Databricks notebook source
# MAGIC %pip install dbtunnel[asgiproxy,chainlit]
# MAGIC %pip install chainlit==1.0.400

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import os

current_directory = os.getcwd()
script_path = current_directory + "/chainlit_example.py"

# COMMAND ----------

from dbtunnel import dbtunnel

dbtunnel.chainlit(script_path).run()

# COMMAND ----------


