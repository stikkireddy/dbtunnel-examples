# Databricks notebook source
# MAGIC %pip install dbtunnel[arize-phoenix,asgiproxy]

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from dbtunnel import dbtunnel
arize = dbtunnel.arize_phoenix()
# make sure to run the next cell to spawn the server
arize.ui_url()


# COMMAND ----------

arize.run()

# COMMAND ----------


