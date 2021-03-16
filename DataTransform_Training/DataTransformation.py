from datetime import datetime
from os import listdir
import pandas
from application_logging.logger import App_Logger
from AzureBlobStorage.azureBlobStorage import AzureBlobStorage

class dataTransform:

     """
               This class shall be used for transforming the Good Raw Training Data before loading it in Database!!.
     """

     def __init__(self):
          self.goodDataPath = 'Training_Good_Raw_Files_Validated'
          self.logger = App_Logger()
          self.azureObj = AzureBlobStorage()


     def replaceMissingWithNull(self):
          """
                       Method Name: replaceMissingWithNull
                       Description: This method replaces the missing values in columns with "NULL" to
                                    store in the table. We are using substring in the first column to
                                    keep only "Integer" data for ease up the loading.
                                    This column is anyways going to be removed during training.
          """
          log_file = 'dataTransformLog'
          try:
               onlyfiles = self.azureObj.listDirFiles(self.goodDataPath)
               for file in onlyfiles:
                    data = self.azureObj.csvToDataframe(self.goodDataPath, file)
                    self.azureObj.saveDataframeToCsv(self.goodDataPath,file,data)
                    self.logger.log(log_file, " %s: Quotes added successfully!!" % file)
          except Exception as e:
               self.logger.log(log_file, "Data Transformation failed because:: %s" % e)